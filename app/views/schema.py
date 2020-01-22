SCHEMAS = {
    "Form": {
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
            "id": {
                "type": "integer",
                "format": "int64",
                "description": "主键"
            },
            "user_id": {
                "type": "integer",
                "format": "int64",
                "description": "创建用户的ID"
            },
            "published_at": {
                "type": "string",
                "format": "date-time",
                "description": "发布日期，如果是null表示取消发布"
            },
            "record_count": {
                "type": "integer",
                "format": "int64",
                "description": "记录的行数",
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
            "fields": {
                "type": "array",
                "items": {
                    "anyOf": [
                        {
                            "$ref": "#/components/schemas/TextField"
                        },
                        {
                            "$ref": "#/components/schemas/SelectField"
                        }
                    ]
                }
            },
        }
    },
    "MultipleMixin": {
        "type": "object",
        "description": "是否是多行或者多选",
        "properties": {
            "multiple": {
                "type": "Boolean",
                "description": "是否是多行或者多选，如果是文本表达多行文本，是checkbox表示多选。"
            },
        }
    },
    "Field": {
        "type": "object",
        "description": "字段的抽象类，具体使用具体查看派生对象。",
        "properties": {
            "id": {
                "type": "integer",
                "format": "int64",
                "description": "主键ID",
            },
            "form_id": {
                "type": "integer",
                "format": "int64",
                "description": "表单的外键ID",
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
                            "$ref": "#/components/schemas/RequiredConstraint"
                        },
                        {
                            "$ref": "#/components/schemas/MinConstraint"
                        },
                        {
                            "$ref": "#/components/schemas/MaxConstraint"
                        },
                        {
                            "$ref": "#/components/schemas/RequiredConstraint"
                        }
                    ]
                }
            },
            "created_at": {
                "type": "string",
                "format": "date-time"
            },
            "updated_at": {
                "type": "string",
                "format": "date-time"
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
    "Option": {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer",
                "format": "int64",
                "description": "主键ID"
            },
            "field_id": {
                "type": "integer",
                "format": "int64",
                "description": "字段的外键ID"
            },
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
            },
            "created_at": {
                "type": "string",
                "format": "date-time"
            },
            "updated_at": {
                "type": "string",
                "format": "date-time"
            }
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
                        "description": "所有选项的集合",
                        "items": {
                            "$ref":  "#/components/schemas/Option",
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
                    },
                    "option_sequence": {
                        "type": "integer",
                        "format": "int64",
                        "description": "保存选项的自增序列"
                    }
                }
            }
        ]
    },
    "Value": {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer",
                "format": "int64",
                "description": "主键ID"
            },
            "sequence": {
                "type": "integer",
                "format": "int64",
                "description": "序号",
            },
            "form_id": {
                "type": "integer",
                "format": "int64",
                "description": "表单外键ID",
            },
            "values": {
                "type": "object",
                "description": "JSON数据"
            },
            "user_id": {
                "type": "integer",
                "format": "int64",
                "description": "用户外键ID，可以是null",
            },
            "ip": {
                "type": "string",
                "description": "提交用户的IP地址",
            },
            "ua_browser": {
                "type": "string",
                "description": "用户浏览器",
            },
            "ua_browser_version": {
                "type": "string",
                "description": "用户浏览器版本",
            },
            "ua_device": {
                "type": "string",
                "description": "用户设备",
            },
            "ua_device_brand": {
                "type": "string",
                "description": "用户设备品牌",
            },
            "ua_device_model": {
                "type": "string",
                "description": "用户设备型号",
            },
            "created_at": {
                "type": "string",
                "format": "date-time"
            },
            "updated_at": {
                "type": "string",
                "format": "date-time"
            }
        }
    },
    "User": {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer",
                "format": "int64",
                "description": "用户主键ID"
            }
        }
    },
    "JWT": {
        "type": "object",
        "properties": {
            "access_token": {
                "type": "string"
            },
            "refresh_token": {
                "type": "string"
            }
        }
    },
    "Signature": {
        "type": "object",
        "properties": {
            "access_key_id": {
                "type": "string",
                "description": "阿里云Access Key ID"
            },
            "policy": {
                "type": "string",
                "description": "阿里云上传策略, base64"
            },
            "signature": {
                "type": "string",
                "description": "阿里云上传签名"
            },
            "key": {
                "type": "string",
                "description": "上传使用的Key"
            },
            "endpoint": {
                "type": "string",
                "description": "阿里云上传的域名"
            },
        }
    },
    "Constraint": {
        "type": "object",
        "properties": {
            "discriminator": {
                "type": "string"
            },
            "id": {
                "type": "integer",
                "format": "int64",
                "description": "主键ID"
            },
            "field_id": {
                "type": "integer",
                "format": "int64",
                "description": "表单的外键ID"
            }
        }
    },
    "RequiredConstraint": {
        "allOf": [
            {
                "$ref": "#/components/schemas/Constraint"
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
    "MinConstraint": {
        "allOf": [
            {
                "$ref": "#/components/schemas/Constraint"
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
    "MaxConstraint": {
        "allOf": [
            {
                "$ref": "#/components/schemas/Constraint"
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
    "RangeConstraint": {
        "allOf": [
            {
                "$ref": "#/components/schemas/Constraint"
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
