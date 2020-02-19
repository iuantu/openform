EDITION_SCHEMAS = {
    "FormEdition": {
        "type": "object",
        "description": "表单模型",
        "discriminator": {
            "propertyName": "discriminator",
            "mapping": {
                "text_field": "#/components/schemas/TextFieldEdition",
                "select_field": "#/components/schemas/SelectFieldEdition"
            },
        },
        "properties": {
            "id": {
                "type": "integer",
                "format": "int64",
                "description": "主键"
            },
            "version": {
                "type": "integer",
                "format": "int64",
                "description": "版本号"
            },
            "title": {
                "type": "string",
                "description": "表单标题"
            },
            "description": {
                "type": "string",
                "description": "表单描述"
            },
            "fields": {
                "type": "array",
                "items": {
                    "anyOf": [
                        {
                            "$ref": "#/components/schemas/TextFieldEdition"
                        },
                        {
                            "$ref": "#/components/schemas/SelectFieldEdition"
                        }
                    ]
                }
            },
        }
    },
    "FieldEdition": {
        "type": "object",
        "description": "字段的抽象类，具体使用具体查看派生对象。",
        "properties": {
            "id": {
                "type": "integer",
                "format": "int64",
                "description": "主键ID",
            },
            "name": {
                "type": "string",
                "description": "只允许A-Za-z0-9-_，并且是字母开头的命名。使用在数据填报场景中的字段英文名"
            },
            "title": {
                "type": "string",
                "description": "字段标题"
            },
            "layout_row_index": {
                "type": "integer",
                "format": "int32",
                "description": "字段所在的行"
            },
            "constraints": {
                "type": "array",
                "description": "字段约束",
                "items": {
                    "anyOf": [
                        {
                            "$ref": "#/components/schemas/RequiredConstraintEdition"
                        },
                        {
                            "$ref": "#/components/schemas/MinConstraintEdition"
                        },
                        {
                            "$ref": "#/components/schemas/MaxConstraintEdition"
                        },
                        {
                            "$ref": "#/components/schemas/RequiredConstraintEdition"
                        }
                    ]
                }
            }
        }
    },
    "TextFieldEdition": {
        "allOf": [
            {
                "$ref": "#/components/schemas/FieldEdition",
            },
            {
                "$ref": "#/components/schemas/MultipleMixin",
            },
            {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64",
                        "description": "主键ID",
                    },
                    "placeholder": {
                        "type": "string",
                        "description": "文本输入的提示文本"
                    },
                    "default": {
                        "type": "string",
                        "description": "默认的文本内容"
                    }
                }
            }
        ]
    },
    "ConstraintEdition": {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer",
                "format": "int64",
                "description": "主键ID"
            },
        }
    },
    "RequiredConstraintEdition": {
        "description": "必须选项约束",
        "allOf": [
            {
                "$ref": "#/components/schemas/ConstraintEdition"
            },
            {
                "type": "object",
                "properties": {
                }
            }
        ]
    },
    "MinConstraintEdition": {
        "description": "最小约束",
        "allOf": [
            {
                "$ref": "#/components/schemas/ConstraintEdition"
            },
            {
                "type": "object",
                "properties": {
                    "min": {
                        "type": "integer",
                        "format": "int64",
                        "description": "最小值，不能小于这个数字。"
                    }
                }
            }
        ]
    },
    "MaxConstraintEdition": {
        "description": "最大约束",
        "allOf": [
            {
                "$ref": "#/components/schemas/ConstraintEdition"
            },
            {
                "type": "object",
                "properties": {
                    "max": {
                        "type": "integer",
                        "format": "int64",
                        "description": "最大值，不能大于这个数字。"
                    }
                }
            }
        ]
    },
    "RangeConstraintEdition": {
        "description": "范围约束",
        "allOf": [
            {
                "$ref": "#/components/schemas/ConstraintEdition"
            },
            {
                "type": "object",
                "properties": {
                    "min": {
                        "type": "integer",
                        "format": "int64",
                        "description": "最小值，不能小于这个数字。"
                    },
                    "max": {
                        "type": "integer",
                        "format": "int64",
                        "description": "最大值，不能大于这个数字。"
                    }
                }
            }
        ]
    }
}

CREATION_SCHEMAS = {
    "FormCreation": {
        "type": "object",
        "description": "表单模型",
        "discriminator": {
            "propertyName": "discriminator",
            "mapping": {
                "text_field": "#/components/schemas/TextField",
                "select_field": "#/components/schemas/SelectField"
            },
        },
        "properties": {
            "title": {
                "type": "string",
                "description": "表单标题"
            },
            "fields": {
                "type": "array",
                "items": {
                    "anyOf": [
                        {
                            "$ref": "#/components/schemas/TextFieldCreation"
                        },
                        {
                            "$ref": "#/components/schemas/SelectFieldCreation"
                        }
                    ]
                }
            },
        }
    },
    "FieldCreation": {
        "type": "object",
        "description": "字段的抽象类，具体使用具体查看派生对象。",
        "properties": {
            "name": {
                "type": "string",
                "description": "只允许A-Za-z0-9-_，并且是字母开头的命名。使用在数据填报场景中的字段英文名"
            },
            "title": {
                "type": "string",
                "description": "字段标题"
            },
            "layout_row_index": {
                "type": "integer",
                "format": "int32",
                "description": "字段所在的行"
            },
            "constraints": {
                "type": "array",
                "description": "字段约束",
                "items": {
                    "anyOf": [
                        {
                            "$ref": "#/components/schemas/RequiredConstraintCreation"
                        },
                        {
                            "$ref": "#/components/schemas/MinConstraintCreation"
                        },
                        {
                            "$ref": "#/components/schemas/MaxConstraintCreation"
                        },
                        {
                            "$ref": "#/components/schemas/RequiredConstraintCreation"
                        }
                    ]
                }
            }
        }
    },
    "TextFieldCreation": {
        "allOf": [
            {
                "$ref": "#/components/schemas/FieldCreation",
            },
            {
                "$ref": "#/components/schemas/MultipleMixin",
            },
            {
                "type": "object",
                "properties": {
                    "discriminator": {
                        "type": "string",
                        "example": "text_field"
                    },
                    "placeholder": {
                        "type": "string",
                        "description": "文本输入的提示文本"
                    },
                    "default": {
                        "type": "string",
                        "description": "默认的文本内容"
                    }
                }
            }
        ]
    },
    "OptionCreation": {
        "type": "object",
        "properties": {
            "label": {
                "type": "string",
                "description": "选项显示的文本内容"
            },
            "value": {
                "type": "integer",
                "description": "选项的值，初始值是1每次新增选项会递增."
            },
            "editable": {
                "type": "boolean",
                "description": "该选项是否可以填写文本内容"
            },
            "ordering": {
                "type": "integer",
                "format": "int64",
                "description": "选项排序的位置"
            }
        }
    },
    "SelectFieldCreation": {
        "allOf": [
            {
                "$ref": "#/components/schemas/FieldCreation",
            },
            {
                "$ref": "#/components/schemas/MultipleMixin",
            },
            {
                "type": "object",
                "properties": {
                    "options": {
                        "type": "array",
                        "description": "所有选项的集合",
                        "items": {
                            "$ref":  "#/components/schemas/OptionCreation",
                        },
                    },
                    "type": {
                        "type": "string",
                        "enum": ["radio", "checkbox"],
                        "description": "类型"
                    },
                    "default": {
                        "type": "array",
                        "description": "默认选中的选项",
                        "items": {
                            "type": "integer",
                            "format": "int64",
                        }
                    }
                }
            }
        ]
    },
    "ConstraintCreation": {
        "type": "object",
        "properties": {
            "discriminator": {
                "type": "string"
            },
        }
    },
    "RequiredConstraintCreation": {
        "allOf": [
            {
                "$ref": "#/components/schemas/ConstraintCreation"
            },
            {
                "type": "object",
                "properties": {
                    "discriminator": {
                        "example" : "required_constraint"
                    },
                }
            }
        ]
    },
    "MinConstraintCreation": {
        "allOf": [
            {
                "$ref": "#/components/schemas/ConstraintCreation"
            },
            {
                "type": "object",
                "properties": {
                    "discriminator": {
                        "example" : "min_constraint"
                    },
                    "min": {
                        "type": "integer",
                        "format": "int64",
                        "description": "最小值，不能小于这个数字。"
                    }
                }
            }
        ]
    },
    "MaxConstraintCreation": {
        "allOf": [
            {
                "$ref": "#/components/schemas/ConstraintCreation"
            },
            {
                "type": "object",
                "properties": {
                    "discriminator": {
                        "example" : "max_constraint"
                    },
                    "max": {
                        "type": "integer",
                        "format": "int64",
                        "description": "最大值，不能大于这个数字。"
                    }
                }
            }
        ]
    },
    "RangeConstraintCreation": {
        "allOf": [
            {
                "$ref": "#/components/schemas/ConstraintCreation"
            },
            {
                "type": "object",
                "properties": {
                    "discriminator": {
                        "example" : "range_constraint"
                    },
                    "min": {
                        "type": "integer",
                        "format": "int64",
                        "description": "最小值，不能小于这个数字。"
                    },
                    "max": {
                        "type": "integer",
                        "format": "int64",
                        "description": "最大值，不能大于这个数字。"
                    }
                }
            }
        ]
    }
}

REQUEST_SCHEMAS = {}
REQUEST_SCHEMAS.update(**CREATION_SCHEMAS)
REQUEST_SCHEMAS.update(**EDITION_SCHEMAS)