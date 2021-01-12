CREATE TABLE appointments(
  id SERIAL primary key,
  name VARCHAR(200) not null,
  start_datetime TIMESTAMP NOT NULL,
  end_datetime TIMESTAMP NOT NULL,
  description TEXT NOT NULL,
  private BOOLEAN NOT NULL
);


INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
VALUES
('My appointment', '2021/12/01 14:00:00', '2021/12/01 15:00:00',
 'An appointment for me', false);
