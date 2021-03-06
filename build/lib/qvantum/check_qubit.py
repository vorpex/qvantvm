﻿'''checking functions for qubit class'''

# pylint: disable=E1101, W1401

def qubit_init_check(function):
    """Decorator to check the arguments of initialization function in qubit class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, alpha, beta):
        """Method to initialize an instance of the qubit class. The squared sum of alpha and beta 
        must be equal to zero otherwise a ValueError will be thrown.
        
        Arguments:
            alpha {int, float, complex} -- Amplitude or probability of being in state 0
            beta {int, float, complex} -- Amplitude or probability of being in state 1
        
        Raises:
            ValueError, TypeError
        
        Examples:
            >>> import math
            >>> import qvantum
            >>>
            >>> q = qvantum.Qubit(1, 0)
            >>> q.show()
            '|Ψ> = (1.0000+0.0000i)|0> + (0.0000+0.0000i)|1>'
            >>> qvantum.Qubit(1 / math.sqrt(2), 1 / math.sqrt(2)).show()
            '|Ψ> = (0.7071+0.0000i)|0> + (0.7071+0.0000i)|1>'
        """

        if all(isinstance(elem, (int, float, complex)) for elem in [alpha, beta]):
            if round(abs(alpha) ** 2 + abs(beta) ** 2 - 1, 10) == 0:
                return function(self, alpha, beta)
        
            else:
                raise ValueError('Invalid input! Alpha and beta must satisfy: ' +\
                    '|alpha|\u00b2 + |beta|\u00b2 = 1.')
        
        else:
            raise TypeError('Invalid input! Alpha and beta must be integer, float or complex.')
    
    return wrapper

def set_amplitudes_check(function):
    """Decorator to check the arguments of setting new amplitudes function in qubit class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, alpha, beta):
        """Setter method to replace the old coefficients to new ones. The squared sum of alpha and 
        beta must be equal to zero otherwise a ValueError will be thrown.
        
        Arguments:
            alpha {int, float, complex} -- Amplitude or probability of being in state 0
            beta {int, float, complex} -- Amplitude or probability of being in state 1
        
        Raises:
            ValueError, TypeError
        
        Examples:
            >>> import math
            >>> import qvantum
            >>>
            >>> q = qvantum.Qubit(1, 0)
            >>> q.show()
            '|Ψ> = (1.0000+0.0000i)|0> + (0.0000+0.0000i)|1>'
            >>> q.set_amplitudes(0, 1)
            >>> q.show()
            '|Ψ> = (0.0000+0.0000i)|0> + (1.0000+0.0000i)|1>'
        """

        if all(isinstance(elem, (int, float, complex)) for elem in [alpha, beta]):
            if round(abs(alpha) ** 2 + abs(beta) ** 2 - 1, 10) == 0:
                return function(self, alpha, beta)
        
            else:
                raise ValueError('Invalid input! Alpha and beta must satisfy: ' +\
                    '|alpha|\u00b2 + |beta|\u00b2 = 1.')
        
        else:
            raise TypeError('Invalid input! Alpha and beta must be integer, float or complex.')
    
    return wrapper
