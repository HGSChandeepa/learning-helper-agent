from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("Web Application C4 Diagram", direction="TB", graph_attr=graph_attr):
    user = Person(
        name="User",
        description="A user of the web application"
    )

    with SystemBoundary("Web Application System"):
        web_app = Container(
            name="Web Application",
            technology="Python and Flask",
            description="Provides the user interface for the application"
        )

        api = Container(
            name="API",
            technology="REST API",
            description="Provides the backend functionality for the application"
        )

        database = Database(
            name="Database",
            technology="PostgreSQL",
            description="Stores application data"
        )
        
        message_queue = Container(
            name="Message Queue",
            technology="RabbitMQ",
            description="Handles asynchronous tasks"
        )

    user >> Relationship("Uses") >> web_app
    web_app >> Relationship("Calls API") >> api
    api >> Relationship("Reads/Writes") >> database
    api >> Relationship("Sends Messages") >> message_queue
