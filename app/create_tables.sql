-- Table: Admin
CREATE TABLE Admin (
    _id integer NOT NULL,
    username text NOT NULL,
    password integer NOT NULL,
    CONSTRAINT Admin_pk PRIMARY KEY (_id)
);

-- Table: Donations
CREATE TABLE Donations (
    _id integer NOT NULL,
    donor_id integer NOT NULL,
    item_id integer NOT NULL,
    quantity integer NOT NULL,
    date date NOT NULL,
    CONSTRAINT Donations_pk PRIMARY KEY (_id),
    CONSTRAINT Donations_Donors FOREIGN KEY (donor_id)
    REFERENCES Donors (_id),
    CONSTRAINT Donations_Items FOREIGN KEY (item_id)
    REFERENCES Items (_id)
);

-- Table: Donors
CREATE TABLE Donors (
    _id integer NOT NULL,
    email text NOT NULL,
    password integer NOT NULL,
    CONSTRAINT Donors_pk PRIMARY KEY (_id)
);

-- Table: Items
CREATE TABLE Items (
    _id integer NOT NULL,
    barcode integer NOT NULL,
    name text NOT NULL,
    weight integer NOT NULL,
    brand text NOT NULL,
    CONSTRAINT Items_pk PRIMARY KEY (_id)
);
