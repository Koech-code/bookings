## SPA BOOKING APP

### Description
> This is an SPA booking web application.
> Customers can book for salon and kinyozi services, cancel the booking. 
> Customers can also leave a feedback after being served. 

## Author

👤 **Author**
- Nixon Kipkorir Koech

- GitHub: [@Koech-code](https://github.com/Koech-code)

## Technologies Used

- HTML
- CSS
- PYTHON `3.6`
- PYTHON SHELL 
- FLASK
- FLASK_BOOTSTRAP
- HEROKU

### User Stories
As a customer I would like to;

- Create an account  
- login to the application
- see the available SPA services
- book a service I want
- cancel a booked service.

## Specifications:
These are the actions the user will do, inputs required and their outputs on the page. 

  | Action    | Input                                      | Output                        |
  | ----------|:-------------                              | :------                       |
  | Load page | On page load                               | Displays the homepage         |
  | Sign up   | email, username, password, confirm password| Redirected to login page      |
  | Login     | username, password                         | Redirect to homepage          |
  | Booking   | book an SPA service                        | Booked service                |
  |           |                                            |                               |
## Live Demo

[Live Demo Link]( https://smartime.herokuapp.com/)


### Installation Process

- Clone the repository using the link below

```
$ git clone https://github.com/Koech-code/booking.git

```

- Create a directory and install the requirements

  ```
  cd app
  pip install -r requirements.txt
  ```
- Export configurations
  ```
  Secrete Key
  Mail_username
  Mail_password
  ```
- Run the application using;
  ```
  python3.6 manage.py server
  ```
- Test it if its working using;
  ```
  python3.6 manage.py test
  ```
- Open the application on your browser , preferably `chrome` using port `127.0.0.1:5000`


## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- I would like to acknowledge Moringa school for giving me this opportunity to learn software development.
- Appreciations to  my TM `Nancy Umutoniwase` for the support she gives me.

## 📝 License

This project is [MIT](LICENCE.md) licensed.