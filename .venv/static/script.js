// const dataSet = [
//     ['Tiger Nixon', 'System Architect', 'Edinburgh', '5421', '2011/04/25', '$320,800'],
//     ['Garrett Winters', 'Accountant', 'Tokyo', '8422', '2011/07/25', '$170,750'],
    
// ];


 
new DataTable('#example', {
    columns: [
        { title: 'ID' },
        { title: 'First NAme' },
        { title: 'Last Name' },
        { title: 'Age' },
        { title: 'Action' },
        
    ],
    // data: dataSet,
    /**i= informcia , flp=ძებნის ველს, rt გამყოფი ხაზი ამის შემდეგ გამეორება შეგიძ₾ია */
    dom: ' <"top"flp> rt <"bottom"flp> <"botton"i><"clear">',
    // ნომრებთან ერთად ემატება next-last velebi
    pagingType: 'full_numbers' ,

    // სქროლს გაუკეთებს მონაცმებს, დავკომენტრე რადგან გვერდბს აქრობს ფალსის გამო
    // paging: false,
    // scrollCollapse: true,
    // scrollY: '50vh'
    initComplete: function () {
        this.api()
            .columns()
            .every(function () {
                let column = this;
                let title = column.footer().textContent;

                // Create input element
                let input = document.createElement('input');
                input.placeholder = title;
                column.footer().replaceChildren(input);

                // Event listener for user input
                input.addEventListener('keyup', () => {
                    if (column.search() !== this.value) {
                        column.search(input.value).draw();
                    }
                });
            });
    },
    
    

});

document.getElementById('toggleButton').addEventListener('click', function () {
    var form = document.getElementById('registrationForm');
    var button = document.getElementById('toggleButton');

    if (form.style.display === 'none') {
        form.style.display = 'block';
        button.innerText = 'Close';
    } else {
        form.style.display = 'none';
        button.innerText = 'Add';
    }
});