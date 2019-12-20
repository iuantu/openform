form_new = {
    'fields': [
        {
            'name': 'gender',
            'label': 'Gender',
            'default': 0,
            'options': [
                {
                    'label': 'Male',
                    'value': 1,
                    'order': 0
                },
                {
                    'label': 'Male',
                    'value': 1,
                    'order': 1
                },
            ],
            'validators': [
                {
                    'type': 'required',
                },
                {
                    'type': 'range',
                    'min': 2,
                    'max': 10,
                }
            ]
        }
    ]
}

form_update = {
    'id': 1,
    'fields': [
        {
            'id': 1,
            'default': 0,
            'options': [
                {
                    'id': 1,
                    'label': 'Male',
                    'value': 1,
                    'order': 0
                },
                {
                    'id': 1,
                    'label': 'Male',
                    'value': 1,
                    'order': 1
                },
            ],
            'validators': [
                {
                    'type': 'required',
                },
                {
                    'type': 'range',
                    'min': 2,
                    'max': 10,
                }
            ]
        }
    ]
}