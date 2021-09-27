import json


class Structure:
    MISSMATCH_TYPES = "Несоответствие типов"
    EMPTY_DATA_OR_STRUCTURE = "Пустые данные или модель данных"
    KEY_NOT_FOUND_ERROR = "Не найден ключ"
    __errors__ = []
    __swagger_types__ = {
        "integer": "<class 'int'>",
        "boolean": "<class 'bool'>",
        "string": "<class 'str'>",
        "object": "<class 'dict'>",
        "null": "<class 'NoneType'>"
    }

    def __checkNullable__(self, data_type, structure_data):
        if data_type == self.__swagger_types__["null"] and "nullable" in structure_data and structure_data["nullable"] == True:
            return False
        return True

    def __checkKeyExist__(self, structure_key, data):
        if not structure_key in data:
            self.__errors__.append(
                {"Тип ошибки": self.KEY_NOT_FOUND_ERROR, "Ожидаемый ключ": key})
            return False
        return True

    def __checkType__(self, data_type, structure_type):
        if data_type != structure_type:
            self.__errors__.append(
                {"Тип ошибки": self.MISSMATCH_TYPES, "Ожидаемый тип": structure_type, "Входящий тип": data_type})
            return False
        return True

    def checkData(self, structure=None, data=None):
        if not isinstance(structure, dict) or not isinstance(data, dict):
            return self.__errors__.append({"type": self.EMPTY_DATA_OR_STRUCTURE})
        for structure_key, structure_data in structure.items():
            structure_type = self.__swagger_types__[
                structure_data["type"].lower()]
            data_type = str(type(data[structure_key]))
            if not self.__checkKeyExist__(structure_key, data):
                continue
            if not self.__checkNullable__(data_type, structure_data):
                continue
            if not self.__checkType__(data_type, structure_type):
                continue
            if data_type == self.__swagger_types__["object"]:
                self.checkData(structure[structure_key]
                               ["properties"], data[structure_key])
        return self

    def getErrors(self):
        return self.__errors__


with open('/home/ashurnasirpal/Рабочий стол/auto_test/Api_Tests/userdata/api_test/temp.json') as temp:
    data = json.load(temp)

errors = Structure().checkData(data["structure"], data["data"]).getErrors()
with open('/home/ashurnasirpal/Рабочий стол/auto_test/Api_Tests/userdata/api_test/outtemp.json', 'w') as out_temp:
    json.dump(errors, out_temp, indent=4, ensure_ascii=False)
