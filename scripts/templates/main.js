$(document).ready(function() {
    // Display user's local time based on the report's UTC timestamp
    function updateLocalTime() {
        // Extract UTC time from the report
        const utcTimeText = $('#utc-time').text();
        // Match pattern like "2025-09-26 05:05:43 UTC"
        const utcMatch = utcTimeText.match(/(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) UTC/);
        
        if (utcMatch) {
            // Parse the UTC time from the report
            const utcTimeString = utcMatch[1];
            // Create date object by adding 'T' and 'Z' for proper ISO format
            const isoString = utcTimeString.replace(' ', 'T') + 'Z';
            const utcDate = new Date(isoString);
            
            // Check if date is valid
            if (!isNaN(utcDate.getTime())) {
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
            } else {
                $('#local-time').text('Invalid date format');
            }
        } else {
            // Fallback - show current time if we can't parse the report time
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