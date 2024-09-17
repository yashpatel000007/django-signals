# Django Signals Demo

This repository demonstrates Django signals, including their synchronous execution, threading behavior, and transaction handling. 

## Project Structure

django-signals-demo/ ├── README.md ├── myapp/ │ ├── init.py │ ├── models.py │ └── views.py # Optional └── manage.py


### `models.py`

Contains the code snippets for:
- **Synchronous Execution:** Shows that Django signals run synchronously.
- **Threading:** Demonstrates that Django signals run in the same thread as the caller.
- **Transaction Handling:** Checks if Django signals run in the same database transaction as the caller.

### Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yashpatel000007/django-signals.git
   cd django-signals
   cd django-signals-demo

2. **Set Up the Virtual Environment**

    ```bash 
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install Dependencies**
    
    ```bash
    pip install django

4. **Apply Migrations**

    Create and apply database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Run the Django Shell**

    Open the Django shell to test the signals:

    ```bash
    python manage.py shell

6. **Execute the Test Code**

    In the Django shell, run the following code to trigger the signal and observe the output:

    ```python
    from myapp.models import MyModel
    print("Creating instance")
    MyModel.objects.create(name="Test")
    print("Instance created")

7. **Expected Output**
    Synchronous Execution: You should see "Signal handler started", followed by "Instance created", and then after a delay, "Signal handler finished".
    Threading: The thread name printed by the signal handler should match the thread name printed by the main code.
    Transaction Handling: The transaction status should be True, indicating the signal runs within the same transaction. 
    