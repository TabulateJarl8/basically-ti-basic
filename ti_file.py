"""
file: ti_file.py
language: python3
author: Nate Levesque <public@thenaterhood.com>
description: Reads and writes TI-Basic .8Xp files and returns
    structures relevant to the file if appropriate.
    
TODO:
    
"""

class tiFile():
    """
    Defines a data object to hold sections of a TI-Basic
    program file
    """
    __slots__=('metadata', 'prgmdata', 'footer')
    
    def __init__(self):
        """
        Initializes the fields of the struct
        to empty fields
        """
        self.metadata='null'
        self.prgmdata='null'
        self.footer='null'
        
    def __str__(self):
        string = "TI File Data Object"
        if (self.metadata != 'null'):
            string += "\n Contains metadata"
        if (self.prgmdata != 'null'):
            string += "\n Contains program data"
        if (self.footer != 'null'):
            string += "\n Contains footer data" 
            
        return string
        
def readFile(filename):
    """
    Reads a TI-Basic .8xp file byte by byte
    and populates the fields of the data object that
    represents it
    
    Arguments:
        filename (str): the filename of a .8xp file to open, inc extension
        
    Returns:
        fileData (tiFile): a tiFile object
        
    """
    
    # Reads the file into an array of bytes
    fileData = tiFile()
    fileContents = []
    with open(filename, "rb") as inStream:
        byte = inStream.read(1)
        while byte:
            byte = inStream.read(1)
            fileContents.append(byte)
    
    # Attempts to extract the metadata and raises an error
    # if the array is too short to contain any
    try:
        fileData.metadata = fileContents[:73]
    except:
        raise RuntimeError("File is too short to be a .8xp file.")
    
    # raises a warning if the array is too short to contain program 
    # data and a footer    
    if (len(fileContents) < 74):
        print("WARNING: File is only long enough to contain metadata.  Will continue, but it might not be pretty")
        fileData.prgmdata = 'null'
        fileData.footer = 'null'
        return fileData
        
    else:
        fileData.prgmdata = fileContents[73:len(fileContents)-4]
        fileData.footer = fileContents[len(fileContents)-4:len(fileContents)]
        
    return fileData
    
def writeFile(filename, tiData):
    """
    Writes a .8xp TI-Basic file to disk as bytes
     
    Arguments:
       filename (str): the name of the file to write
       tiData (tiFile): a tiFile object to write the data for
        
    Returns:
        fileWritten (boolean): a boolean value of whether or not the file
            has been written
    """
    
    # Add the .8xp extension to the filename
    filename = (filename.split('.')[0] + ".8Xp")
    
    # Opens the file to write binary
    outFile = open(filename, "wb")
    
    # Writes the metadata to the file
    for byte in tiData.metadata:
        if (isinstance(byte, bytes)):
            outFile.write(byte)
        else:
            print("Error writing byte to file.  Was string '"+byte+"'.  Continuing, but compiled file might have problems.")
    
    # Writes the program data to the file            
    for byte in tiData.prgmdata:
        if (isinstance(byte, bytes)):
            outFile.write(byte)
        if (not isinstance(byte, bytes)):
            print("Error writing byte to file.  Was string '"+byte+"'.  Continuing, but compiled file might have problems.")
    
    # Writes the footer to the file (can be an emptylist, file
    # does not seem to rely on footer)
    for byte in tiData.footer:
        if (isinstance(byte, bytes)):
            outFile.write(byte)
        if (not isinstance(byte, bytes)):
            print("Error writing byte to file.  Was string '"+byte+"'.  Continuing, but compiled file might have problems.")
    
    # Returns true for now, will later possibly perform some check to
    # make sure it wrote what it intended.  For now needs to just
    # write the whole thing or fail, makes it easier to debug the encode
    # function if a big problem pops up        
    return True

