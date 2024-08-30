# VenuePlanner with Whatsapp Message

This project provides a seamless venue booking experience for customers. Customers can submit booking requests based on their desired date, and the venue, which serves as a backend, has the option to accept or reject the request. Once a booking is confirmed, a WhatsApp message is automatically sent to both the customer and the venue, notifying them of the decision. This streamlined communication process ensures efficient coordination between all parties involved.


## Features

- Easy venue booking process
- User registration for venues and customers
- Edit profile functionality for users
- Customers can send booking requests with their desired date
- Venues can accept or reject booking requests from customers
- WhatsApp message sent to both customer and venue based on booking decision


## Installation

1. Clone the repository: `git clone https://github.com/your-username/venue-booking.git`
2. Navigate to the project directory: `cd venue-booking`
3. Install dependencies: `pip install -r requirements-dev.txt`

## Usage

1. Open the project in your preferred code editor.
2. Configure the WhatsApp API credentials in the `.env` file.
3. Run the application: `python manage.py runserver`
4. Access the application in your web browser at `http://localhost:8000`

### Endpoints
- API Documentation: `/api/schema/swagger-ui/`

## Contributing

Contributions are welcome! Please follow the guidelines outlined in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
