import math


def complement_rgb(rgb):
    """
    Returns: the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # THIS IS WRONG.  FIX IT
    assert type(rgb) == cornell.RGB
    return cornell.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def round(number, places):
    """
    Returns: the number rounded to the given number of decimal places.
    
    The value returned is a float.
    
    This function is more stable than the built-in round.  The built-in round
    has weird behavior where round(100.55,1) is 100.5 while round(100.45,1) is
    also 100.5.  We want to ensure that anything ending in a 5 is rounded UP.
    
    It is possible to write this function without the second precondition on
    places. If you want to do that, we leave that as an optional challenge.
    
    Parameter number: the number to round to the given decimal place
    Precondition: number is an int or float
    
    Parameter places: the decimal place to round to
    Precondition: places is an int; 0 <= places <= 3
    """
    # To get the desired output, do the following
    #   1. Shift the number "to the left" so that the position to round to is left of 
    #      the decimal place.  For example, if you are rounding 100.556 to the first 
    #      decimal place, the number becomes 1005.56.  If you are rounding to the second 
    #      decimal place, it becomes 10055.6.  If you are rounding 100.556 to the nearest 
    #      integer, it remains 100.556.
    #   2. Add 0.5 to this number
    #   3. Convert the number to an int, cutting it off to the right of the decimal.
    #   4. Shift the number back "to the right" the same amount that you did to the left.
    #      Suppose that in step 1 you converted 100.556 to 1005.56.  In this case, 
    #      divide the number by 10 to put it back.
    
    try:
      assert type(number) == int
    except:
      assert type(number) == float
    
    assert type(places)==int
    assert 0<= places and places <=3
    
    #step 1
    temp = number * (10**places) 
    print('step 1 value is ' + repr(temp))

    #step 2
    temp = temp + 0.5
    print('step 2  value is '+repr(temp))
    
    #step3
    temp = int(temp)
    print('step 3 value is '+ repr(temp))
    
    #step4
    temp = temp/(10.0**places)
    print('step 4 value is ' + repr(temp))
    
    print('rounding '+repr(number)+' to '+ repr(places) + ' is '+ repr(temp))
    return temp


def str5(value):
    """
    Returns: value as a string, but expand or round to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Note:Obviously, you want to use the function round() that you just defined. 
    # However, remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.
    try:
      assert type(value) == int
    except:
      assert type(value) == float

    assert 0<= value and value <=360
    
    str_value = str(value)
    if(str_value.find('e') != -1):
        #ex: 0.0000001 --> 1e-06
        return '0.000'
    
    print('str_value is '+str_value)
    
    if(len(str_value) == 5):
        str_value = str_value[0:5]
        print('the value has 5 characters and is '+str_value)
    elif(len(str_value) < 5):
        val = float(value)
        str_value = str(val)
        num_zeros = 5 - len(str_value)
        if(num_zeros == 1):
        	str_value = str_value + '0'
        elif(num_zeros == 2):
        	str_value = str_value + '00'
    elif(len(str_value) > 5):
        places = 5-(str_value.index('.')+1)
        value = round(value, places)
        str_value  = str(value)
        num_zeros = 5 - len(str_value)
        if(len(str_value) < 5):
            val = float(value)
            str_value = str(val)
            num_zeros = 5 - len(str_value)
        if(num_zeros == 1):
        	str_value = str_value + '0'
        elif(num_zeros == 2):
        	str_value = str_value + '00'
        print('the value with 5 charaters is'+str_value)
 
      
    return str_value   


def str5_cmyk(cmyk):
    """
    Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmtk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    assert type(cmyk) == cornell.CMYK
    str_cmyk = str(cmyk)
    print('str_cmyk is' +str_cmyk)
    a = str_cmyk.index(',')
    c = str_cmyk[1:a]
    print(c)
    print('str_cmyk is' +str_cmyk)
    b = str_cmyk.index(',', a+1)
    m = str_cmyk[a+1: b]
    print(repr(a+1) + ' ' + repr(b) + ' ' + m)
    d = str_cmyk.index(',', b+1)                     
    y = str_cmyk[b+1: d]  
    k = str_cmyk[d+1:-1]
                         
    c = str5(float(c))
    m = str5(float(m))
    y = str5(float(y))
    k = str5(float(k))
    
    str5CMYK = '(' + c + ', ' + m + ', ' + y + ', ' + k + ')'
    print('str5_cmyk returns ' + repr(str5CMYK))
    
    return str5CMYK


def str5_hsv(hsv):
    """
    Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    assert type(hsv) == cornell.HSV
    str_hsv = str(hsv)
    a = str_hsv.index(',')
    h = str_hsv[1:a]
    b = str_hsv.index(',', a+1)
    s = str_hsv[a+1: b]
    v = str_hsv[b+1:-1]
    
    h = str5(float(h))
    s = str5(float(s))
    v = str5(float(v))  
    str5HSV = '(' + h + ', ' + s + ', ' + v + ')'
    return str5HSV


def rgb_to_cmyk(rgb):
    """
    Returns: color rgb in space CMYK, with the most black possible.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change the RGB numbers to the range 0..1 by dividing them by 255.0.
    assert type(rgb) == cornell.RGB
   
    r_prime = rgb.red/255.0
    g_prime = rgb.green/255.0
    b_prime = rgb.blue/255.0
    print('r-g primes are '+repr(r_prime)+', ' +repr(g_prime)+', '+repr(b_prime))
    
    c_prime = 1 - r_prime
    m_prime = 1 - g_prime
    y_prime = 1 - b_prime
    print('c-y primes are '+repr(c_prime)+', ' +repr(m_prime)+', '+repr(y_prime))
    
    if(c_prime == 1 and m_prime == 1 and y_prime == 1):
        c = 0
        m = 0
        y = 0
        k = 1
    else:
        k = min(c_prime, m_prime , y_prime)
        c = (c_prime - k)/(1 - k)
        m = (m_prime - k)/(1 - k)
        y = (y_prime - k)/(1 - k)
        
    print('c, m, y, k are '+repr(c)+', '+repr(m) +', ' + repr(y) +', ' + repr(k))
    
    cmyk = cornell.CMYK(0.0,0.0,0.0,0.0)
    cmyk.cyan = 100*c
    cmyk.magenta = 100*m
    cmyk.yellow = 100*y
    cmyk.black = 100*k
    
    str5_cmyk(cmyk)
    
    return cmyk


def cmyk_to_rgb(cmyk):
    """
    Returns : color CMYK in space RGB.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0.  Deal with them in the 
    # same way as the RGB numbers in rgb_to_cmyk()
    assert type(cmyk) == cornell.CMYK
    
    c_prime = cmyk.cyan/100.0
    m_prime = cmyk.magenta/100.0
    y_prime = cmyk.yellow/100.0    
    k_prime = cmyk.black/100.0
    
    r_prime = (1 - c_prime)*(1 - k_prime)
    g_prime = (1 - m_prime)*(1 - k_prime)
    b_prime = (1 - y_prime)*(1 - k_prime)
    
    rgb = cornell.RGB(0,0,0)
    
    rgb.red = int(round(255.0*r_prime, 0))
    rgb.green = int(round(255.0*g_prime, 0))
    rgb.blue = int(round(255.0*b_prime, 0))

    return rgb 


def rgb_to_hsv(rgb):
    """
    Return: color rgb in HSV color space.
    
    Formulae from wikipedia.org/wiki/HSV_color_space.
   
    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    assert type(rgb) == cornell.RGB   
    
    r_prime = rgb.red/255.0
    g_prime = rgb.green/255.0
    b_prime = rgb.blue/255.0
    print('r-g primes are '+repr(r_prime)+', ' +repr(g_prime)+', '+repr(b_prime))
    
    MAX = max(r_prime, g_prime, b_prime)
    MIN = min(r_prime, g_prime, b_prime)
    
    if(MAX == MIN):
        H = 0
    elif(MAX == r_prime and g_prime >= b_prime):
        H = 60.0*(g_prime-b_prime)/(MAX-MIN)
    elif(MAX == r_prime and g_prime < b_prime):
        H = 60.0*(g_prime-b_prime)/(MAX-MIN) + 360.0
    elif(MAX == g_prime):
        H = 60.0*(g_prime-b_prime)/(MAX-MIN) + 120.0
    elif(MAX == b_prime):
        H = 60.0*(g_prime-b_prime)/(MAX-MIN) + 240.0
    
    if(MAX == 0):
        S = 0
    else:
        S = 1 - MIN/MAX
        
    V = MAX
    
    hsv = cornell.HSV(0.0,0.0,0.0)
    hsv.hue = H
    hsv.saturation = S
    hsv.value = V
    return hsv 


def hsv_to_rgb(hsv):
    """
    Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    assert type(hsv) == cornell.HSV
    
    h_prime = math.floor(hsv.hue/60)
    f = hsv.hue/60 - h_prime
    p = hsv.value*(1-hsv.saturation)
    q = hsv.value*(1-f*hsv.saturation)
    t = hsv.value*(1-(1-f)*hsv.saturation)
   
    if(h_prime == 0):
        R = hsv.value
        G = t
        B = p
    elif(h_prime == 1):
        R = q
        G = hsv.value
        B = p
    elif(h_prime == 2):
        R = p
        G = hsv.value
        B = t
    elif(h_prime == 3):
        R = p
        G = q
        B = hsv.value
    elif(h_prime == 4):
        R = t
        G = p
        B = hsv.value
    elif(h_prime == 5):
        R = hsv.value
        G = p
        B = q
       
    rgb = cornell.RGB(0,0,0) 
    rgb.red = int(round(255.0*R, 0))
    rgb.green = int(round(255.0*G, 0))
    rgb.blue = int(round(255.0*B, 0))
    
    return rgb      
