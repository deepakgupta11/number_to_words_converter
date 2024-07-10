
Design a Django-based web application that allows the end user to write numerals as well as words in both English and Hindi. This tool enables the user to generate text representations of numbers when writing cheques.

**Features**
- **Input Form**: This is the form that accepts numerical amounts between Re 1 to Rs 99,99,99,999.
- **Language Support**: It will convert the amounts to both English and Hindi words.
- **User Interface**: Simple and intuitive web interface for input and output.

**Tech Stack**
- **Backend**: Django
- **Frontend**: HTML, CSS
- **Libraries**:
  - num2words for English conversion
  - Custom function for Hindi conversion

**File Structure**
- **cheque_app**: Main Django project directory
- **converter**: App directory
  - **forms.py**: Contains the input form
  - **views.py**: Accepts input in the form and processes it
  - **utils.py**: Contains the conversion logic
  - **urls.py**: URL routing
  - **templates**: HTML templates
    - **converter/index.html**: Input form template
    - **converter/result.html**: Result display template

**Implementation Details**
- **Forms**:
  - **AmountForm**: A Django form to accept amount input
- **Views**:
  - **convert_amount**: A view to accept the input and render the result
- **Utilities**:
  - **number_to_words_hindi**: A custom utility to convert the number into Hindi words
  - **number_to_words**: A utility that handles the conversion for each language
- **Templates**:
  - **index.html**: The main template that contains the form elements
  - **result.html**: The template that renders the output from the conversion

**Usage**
- **Run the Server**:
  ```bash
  python manage.py runserver
  ```
- **Access the Application**:
  Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Convert Amounts**:
  Type an amount and see the converted result for both languages.
