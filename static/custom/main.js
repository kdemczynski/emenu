$(document).ready(function ($) {

            $(".clickable_row").click(function () {
                window.document.location = $(this).data("href");
            }); // clickable end

            $('#table_sort').dataTable({
                "paging":   true,
                "info":     false,
                "searching":   true,
                "language": {
                    "lengthMenu": "Pokazuj _MENU_ rekordów na stronę",
                    "zeroRecords": "Nie znaleziono żadnych rekordów",
                    "info": "Strona _PAGE_ z _PAGES_",
                    "infoEmpty": "Nie znaleziono żadnych rekordów",
                    "search": "Szukaj w tabeli:",
                    "paginate": {
                        "first": "Pierwsza",
                        "last": "Ostatnia",
                        "next": "Następna",
                        "previous": "Poprzednia"
                    }
                },
            });

}); //document end