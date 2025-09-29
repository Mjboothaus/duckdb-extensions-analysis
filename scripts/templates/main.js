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
            
            // Add special sorting for Status column if present
            if (numCols >= 4) {
                columnDefs.push({
                    // Status column is typically at index 3
                    "targets": [3],
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
            
            $table.DataTable({
                "pageLength": 25,
                "lengthMenu": [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
                "order": [],
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