SCHEMAS = {
    "Form": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
            },
            "fields": {
                "type": "array",
                "items": {
                    "$ref":  "#/components/schemas/Field",
                },
            },
        }
    },
    "MultipleMixin": {
        "type": "object",
        "properties": {
            "multiple": {
                "type": "Boolean",
            },
        }
    },
    "Field": {

        "type": "object",
        "discriminator": {
            "propertyName": "discriminator",
            "mapping": {
                "text_field": "#/components/schemas/TextField"
            },
        },
        "properties": {
            "id": {
                "type": "integer"
            },
            "name": {
                "type": "string"
            },
            "discriminator": {
                "type": "string",
            }
        }
    },
    "TextField": {
        "allOf": [
            {
                "$ref": "#/components/schemas/Field",
            },
            {
                "$ref": "#/components/schemas/MultipleMixin",
            },
            {
                "type": "object",
                "properties": {
                    "placeholder": {
                        "type": "string"
                    },
                    "default": {
                        "type": "string"
                    }
                }
            }
        ]
    },
    "Option": {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer"
            },
            "field_id": {
                "type": "integer"
            },
            "label": {
                "type": "string"
            },
            "value": {
                "type": "integer"
            },
        }
    },
    "SelectField": {
        "allOf": [
            {
                "$ref": "#/components/schemas/Field",
            },
            {
                "$ref": "#/components/schemas/MultipleMixin",
            },
            {
                "type": "object",
                "properties": {
                    "options": {
                        "type": "array",
                        "items": {
                            "$ref":  "#/components/schemas/Option",
                        },
                    },
                    "default": {
                        "type": "integer"
                    }
                }
            }
        ]
    },
}
