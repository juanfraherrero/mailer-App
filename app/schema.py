instructions = [
    'DROP TABLE IF EXISTS email;',
    """
        CREATE TABLE email(
                id SERIAL PRIMARY KEY,
                email VARCAHAR(50) NOT NULL,
                subject VARCAHAR(50) NOT NULL,
                content VARCAHAR(500) NOT NULL
        );
    """

]