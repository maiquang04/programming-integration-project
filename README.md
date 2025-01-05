# **programming-integration-project**

## **How to Run**

1. **Verify the project directory contents:**

    ```
    ls
    ```

    You should see:

    - `retail/`
    - `db.sqlite3`
    - `manage.py` (Django’s management script)

    If these are not present, recheck your directory structure.

2. **Install necessary packages**

    ```
    pip install -r requirements.txt
    ```

3. **Run the development server:**

    ```
    python manage.py runserver
    ```

4. **Access the website:**
   Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## **To Access Specific Pages Example**

-   **Checkout Page:**  
    [http://127.0.0.1:8000/checkout/](http://127.0.0.1:8000/checkout/)

-   **Product Details Page:**  
    [http://127.0.0.1:8000/product-details/](http://127.0.0.1:8000/product-details/)

## **Accounts**

-   For customers, they may register their own accounts.

-   Admin at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin), username: admin, password: admin.

## **Specifications**

-   Login / Log out
-   Search
-   View product details
-   Filter by category
-   Responsive main page
-   Wishlist
-   Cart
-   Checkout
