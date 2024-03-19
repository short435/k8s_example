# Created by Zhen-Yi Yu on 2024/03/19

from app import create_app
import logging

app = create_app()

if __name__ != '__main__':
	gunicorn_logger = logging.getLogger('gunicorn.error')
	app.logger.handlers = gunicorn_logger.handlers
	app.logger.setLevel(gunicorn_logger.level)

if __name__ == '__main__':
    
	app.run(debug=True, host='0.0.0.0', port=3000)
