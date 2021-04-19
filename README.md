# Shuup Mailer
### Modifications
- Move dataloader CLI to core app bootstrap CLI
- Cache mailer index page in database table
- Use Django ORM for count and sum calculations
- Load settings from environment variables to follow the 12 factor app pattern
- Logging configuration
- Celery for async task processing
- Dockerized Redis for Celery backend
- Bootstrap.js
- Restructure project
- Register mailer app models for Django admin
