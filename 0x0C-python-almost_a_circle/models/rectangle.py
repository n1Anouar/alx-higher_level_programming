from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x coordinate of the rectangle. Defaults to 0.
            y (int, optional): y coordinate of the rectangle. Defaults to 0.
            id (int, optional): id of the instance. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute

        Args:
            value (int): new value for the width attribute
        """
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute

        Args:
            value (int): new value for the height attribute
        """
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute

        Args:
            value (int): new value for the x attribute
        """
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute

        Args:
            value (int): new value for the y attribute
        """
        self.__y = value
