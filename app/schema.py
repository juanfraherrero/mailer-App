instructions = [
    'DROP TABLE IF EXISTS email;',
    """
        CREATE TABLE email(
                id SERIAL PRIMARY KEY,
                email VARCHAR(50) NOT NULL,
                subject VARCHAR(50) NOT NULL,
                content VARCHAR(500) NOT NULL
        );
    """

]