from project_manager.app import create_app


def init_app():
    flask_app = create_app()

    flask_app.run(debug=True)

if __name__ == '__main__':
    init_app()