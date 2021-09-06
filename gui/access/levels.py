'''
ADD A DICTIONARY ENTRY FOR EACH LEVEL TO BE GRANTED
Top-levle dir: "levels"
Level prefix: MI
 ## EVERY TIME A BUTTON IS ADDED THIS LIST (AT LEAST MI7) SHOULD BE UPDATED TO ACCOUNT FOR IT ##
 Page number 9 is reserved for Welcome View [Page not button 9]
'''

Access = {"level": {
    "MI0": {"pages": [2, 10],
            "login_request": ["utsa.makerspace.outreach@gmail.com", "be@m@kerUT5@out"]},
    "MI1": {"pages": [2, 10],
            "login_request": ["utsa.makerspace.financial@gmail.com", "be@m@kerUT5@fin"]},
    "MI2": {"pages": [0, 10],
            "login_request": ["utsa.makerspace.machine.staff@gmail.com", "be@m@kerUT5@staff"]},
    "MI3": {"pages": [2, 10],
            "login_request": ["utsa.makerspace.operations@gmail.com", "be@m@kerUT5@op"]},
    "MI4": {"pages": [2, 10],
            "login_request": {"utsa.makerspace.president@gmail.com", "be@m@kerUT5@pres"}},
    "MI5": {"pages": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "login_request": ["utsa.makerspace@gmail.com", "be@m@kerUT5@"]},
    "MI6": {"pages": [], "login_request": None},
    "MI7": {"pages": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "login_request": ["utsa.makerspace@gmail.com", "be@m@kerUT5@"]},
}
}

"""
        Button Access                         Number
Machine Shop Monday.com Dashboard               0
Machine Shop Safety Documents                   1
3D Printing Monday.com Dashboard                2
Inventory - Overview                            3
Inventory - Search                              4
Inventory - Update                              5
Inventory - Append                              6
Inventory - Approve                             7
Inventory - Denied                              8
General Monday.com                              9
Logout                                          10
"""