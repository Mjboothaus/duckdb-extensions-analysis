$(document).ready(function() {
    // Display user's local time based on the report's UTC timestamp
    function updateLocalTime() {
        // Extract UTC time from the report
        const utcTimeText = $('#utc-time').text().trim();
        console.log('UTC time text:', utcTimeText);
        
        // Try multiple patterns for timestamp matching
        const patterns = [
            /(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) UTC/,  // "2025-09-26 05:05:43 UTC"
            /(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})/,      // "2025-09-26 05:05:43" (assume UTC)
            /Report Generated:\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) UTC/,
            /Last Updated:\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) UTC/
        ];
        
        let utcTimeString = null;
        for (const pattern of patterns) {
            const match = utcTimeText.match(pattern);
            if (match) {
                utcTimeString = match[1];
                console.log('Matched timestamp:', utcTimeString);
                break;
            }
        }
        
        if (utcTimeString) {
            // Try different parsing methods
            let utcDate = null;
            
            // Method 1: ISO format with Z
            try {
                const isoString = utcTimeString.replace(' ', 'T') + 'Z';
                utcDate = new Date(isoString);
                console.log('Parsed ISO:', isoString, utcDate);
            } catch (e) {
                console.log('ISO parsing failed:', e);
            }
            
            // Method 2: Direct parsing with explicit UTC
            if (!utcDate || isNaN(utcDate.getTime())) {
                try {
                    utcDate = new Date(utcTimeString + ' UTC');
                    console.log('Parsed with UTC suffix:', utcDate);
                } catch (e) {
                    console.log('UTC suffix parsing failed:', e);
                }
            }
            
            // Check if date is valid
            if (utcDate && !isNaN(utcDate.getTime())) {
                try {
                    // Convert to local time with same format as UTC
                    const year = utcDate.getFullYear();
                    const month = String(utcDate.getMonth() + 1).padStart(2, '0');
                    const day = String(utcDate.getDate()).padStart(2, '0');
                    const hour = String(utcDate.getHours()).padStart(2, '0');
                    const minute = String(utcDate.getMinutes()).padStart(2, '0');
                    const second = String(utcDate.getSeconds()).padStart(2, '0');
                    const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
                    const localTimeString = `${year}-${month}-${day} ${hour}:${minute}:${second} ${timeZone}`;
                    $('#local-time').text(localTimeString);
                    console.log('Local time set:', localTimeString);
                    return;
                } catch (e) {
                    console.log('Locale formatting failed:', e);
                }
            }
        }
        
        // Fallback - show current time if parsing fails
        console.log('Using fallback current time');
        try {
            const now = new Date();
            const localTimeString = now.toLocaleString('en-AU', {
                year: 'numeric',
                month: '2-digit', 
                day: '2-digit',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
                timeZoneName: 'short'
            });
            $('#local-time').text(localTimeString + ' (current)');
        } catch (e) {
            $('#local-time').text('Time unavailable');
        }
    }
    
    // Update local time once (it's static based on report time)
    updateLocalTime();
    
    // Make tables interactive with appropriate configurations
    $('table').addClass('table table-striped table-hover');
    
    // Configure tables based on their content and context  
    $('table').each(function() {
        const $table = $(this);
        
        // Find the preceding heading to determine table type
        const $prevHeading = $table.prevAll('h1, h2, h3, h4').first();
        const headingText = $prevHeading.text() || '';
        
        // Check number of columns in header
        const numCols = $table.find('thead tr:first th').length;
        
        // Determine if this is a static table (Summary, Historical Releases)
        const isStaticTable = headingText.includes('Summary') || 
                             headingText.includes('Historical Releases') || 
                             headingText.includes('Current Release Context') ||
                             numCols <= 3;
        
        console.log(`Table under "${headingText}" has ${numCols} columns, isStatic: ${isStaticTable}`);
        
        if (isStaticTable) {
            // Static tables: minimal functionality
            const needsSearch = headingText.includes('Historical');
            $table.DataTable({
                "paging": false,
                "lengthChange": false,
                "info": false,
                "searching": needsSearch,
                "order": [],
                "responsive": true,
                "dom": needsSearch ? 'ft' : 't'
            });
        } else {
            // Interactive extension tables: full functionality
            let columnDefs = [{ "orderable": true, "targets": "_all" }];
            
            // Add custom sorting for extension tables
            // Determine column indices dynamically
            const headers = $table.find('thead tr:first th').map(function() {
                return $(this).text().trim();
            }).get();
            
            const statusIdx = headers.indexOf('Status');
            const starsIdx = headers.indexOf('Stars');
            const activityIdx = headers.indexOf('Last Activity');
            
            // Status column: Sort by icon type
            if (statusIdx >= 0) {
                columnDefs.push({
                    "targets": [statusIdx],
                    "type": "string",
                    "render": function(data, type, row) {
                        if (type === 'sort' || type === 'type') {
                            if (data && typeof data === 'string') {
                                if (data.includes('🟢')) return '1-Ongoing';
                                if (data.includes('❓')) return '2-Unknown';
                                if (data.includes('🔴')) return '3-Discontinued';
                                if (data.includes('⚠️')) return '4-Issues';
                                return '5-Other';
                            }
                        }
                        return data;
                    }
                });
            }
            
            // Stars column: Extract numeric value from text
            if (starsIdx >= 0) {
                columnDefs.push({
                    "targets": [starsIdx],
                    "type": "num",
                    "render": function(data, type, row) {
                        if (type === 'sort' || type === 'type') {
                            if (data && typeof data === 'string') {
                                // Handle "N/A" cases
                                if (data.includes('N/A') || data.includes('NOT FOUND')) {
                                    return -1; // Sort N/A to bottom
                                }
                                // Extract first number from string
                                const match = data.match(/\d+/);
                                return match ? parseInt(match[0]) : -1;
                            }
                            return data || -1;
                        }
                        return data;
                    }
                });
            }
            
            // Last Activity column: Parse relative and absolute dates
            if (activityIdx >= 0) {
                columnDefs.push({
                    "targets": [activityIdx],
                    "type": "num",
                    "render": function(data, type, row) {
                        if (type === 'sort' || type === 'type') {
                            if (data && typeof data === 'string') {
                                const now = Date.now();
                                const dayMs = 24 * 60 * 60 * 1000;
                                
                                // Handle "today"
                                if (data.toLowerCase().includes('today')) {
                                    return now;
                                }
                                
                                // Handle "X days ago"
                                const daysMatch = data.match(/(\d+)\s+days?\s+ago/);
                                if (daysMatch) {
                                    return now - (parseInt(daysMatch[1]) * dayMs);
                                }
                                
                                // Handle absolute dates (YYYY-MM-DD HH:MM:SS UTC)
                                const dateMatch = data.match(/(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})/);
                                if (dateMatch) {
                                    try {
                                        return new Date(dateMatch[1] + ' UTC').getTime();
                                    } catch (e) {
                                        return 0;
                                    }
                                }
                                
                                // Fallback
                                return 0;
                            }
                            return 0;
                        }
                        return data;
                    }
                });
            }
            
            // Set default sort order: by Extension name (column 1) ascending
            const extensionIdx = headers.indexOf('Extension');
            const defaultOrder = extensionIdx >= 0 ? [[extensionIdx, 'asc']] : [];
            
            $table.DataTable({
                "pageLength": 25,
                "lengthMenu": [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
                "order": defaultOrder,
                "columnDefs": columnDefs,
                "responsive": true,
                "dom": '<"top"lf>rt<"bottom"ip><"clear">'
            });
        }
    });
    
    // Add timezone info tooltip after tables are initialized
    setTimeout(function() {
        $('#local-time').attr('title', 'Report time in your local timezone');
        
        // Make all links in tables open in new tabs
        $('table a').attr('target', '_blank').attr('rel', 'noopener noreferrer');
    }, 100);
});