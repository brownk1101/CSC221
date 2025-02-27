class Person:
    def __init__(self, first, last, phone):
        """Initializes Person object."""
        self.__first = first
        self.__last = last
        self.__phone = phone

    def set_first(self, name):
        """Sets first name for object.

        Parameters
        ----------
        name: str
            Name to set for first name.
        """
        self.__first = name

    def set_last(self, last):
        """Sets last name for object.

        Parameters
        ----------
        name: str
            Name to set for last name.
        """
        self.__last = last

    def set_phone(self, phone):
        """Sets phone number for object.

        Parameters
        ----------
        phone: str
            Phone number to set.
        """
        self.__phone = phone
    
    def get_first(self):
        """Gets first name for object.

        Returns
        -------
        str
            First name.
        """
        return self.__first
        
    def get_last(self):
        """Gets last name for object.

        Returns
        -------
        str
            Last name.
        """
        return self.__last
    
    def get_phone(self):
        """Gets phone number.

        Returns
        -------
        str
            Phone number.
        """
        return self.__phone
    
    def __repr__(self):
        """Returns string representation of object."""
        return f'{self.__first:<20}{self.__last:<20}{self.__phone:<20}'

class Customer(Person):
    def __init__(self, first, last, phone, email, state, address):
        """Initializes Customer object."""
        Person.__init__(self, first, last, phone)
        self.__email = email
        self.__state = state
        self.__address = address
 
     
    #Setters
    def set_email(self, email):
        """Sets email for object.

        Parameters
        ----------
        email: str
            email to set.
        """
        self.__email = email
    def set_state(self, state):
        """Sets state for object.

        Parameters
        ----------
        state: str
            state to set.
        """
        self.__state = state
    def set_address(self, address):
        """Sets address for object.

        Parameters
        ----------
        address: str
            address to set.
        """
        self.__address = address
  
    #Getters   
    def get_email(self):
        """Gets email for object.

        Returns
        -------
        str
            email address.
        """
        return self.__email

    def get_address(self):
        """Gets address for object.

        Returns
        -------
        str
            street address.
        """
        return self.__address
    
    def get_state(self):
        """Gets state for object.

        Returns
        -------
        str
            state.
        """
        return self.__state
    
    def __repr__(self):
        """Returns string representation of object."""
        return Person.__repr__(self)+f'{self.__email:<20}{self.__address:<20}{self.__state}'
