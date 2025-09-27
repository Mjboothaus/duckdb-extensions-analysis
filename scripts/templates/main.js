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
                    // Convert to local time
                    const localTimeString = utcDate.toLocaleString('en-AU', {
                        year: 'numeric',
                        month: '2-digit', 
                        day: '2-digit',
                        hour: '2-digit',
                        minute: '2-digit',
                        second: '2-digit',
                        timeZoneName: 'short'
                    });
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
    
    // Configure static tables (Summary, Historical Releases) differently
    $('table').each(function() {
        const $table = $(this);
        const isStaticTable = $table.closest('h2, h3').prev().text().includes('Summary') || 
                             $table.closest('h2, h3').prev().text().includes('Historical Releases');
        
        if (isStaticTable) {
            // Static tables: no pagination, no length menu, but keep search for Historical
            const isHistorical = $table.closest('h2, h3').prev().text().includes('Historical');
            $table.DataTable({
                "paging": false,
                "lengthChange": false,
                "info": false,
                "searching": isHistorical,
                "order": [],
                "responsive": true,
                "dom": isHistorical ? 'ft' : 't'
            });
        } else {
            // Interactive tables: full functionality
            $table.DataTable({
                "pageLength": 25,
                "lengthMenu": [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
                "order": [],
                "columnDefs": [
                    { "orderable": true, "targets": "_all" }
                ],
                "responsive": true,
                "dom": '<"top"lf>rt<"bottom"ip><"clear">'
            });
        }
    });
    
    // Add timezone info tooltip after tables are initialized
    setTimeout(function() {
        $('#local-time').attr('title', 'Report time in your local timezone');
    }, 100);
});