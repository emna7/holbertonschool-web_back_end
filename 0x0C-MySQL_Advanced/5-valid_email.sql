-- trigger that resets the attribute valid email when email is changed
DELIMITER $$

CREATE TRIGGER email_address
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
