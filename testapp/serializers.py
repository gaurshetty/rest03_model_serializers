from rest_framework import serializers
from .models import Employee


def multiple_of_thousands(value):
    print('validation by validator attr')
    if value % 1000 != 0:
        raise serializers.ValidationError("Salary should be multiple of 1000")


class EmployeeSerializers(serializers.ModelSerializer):
    salary = serializers.FloatField(validators=[multiple_of_thousands, ])
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_salary(self, value):
        print("Field validation")
        if value < 5000:
            raise serializers.ValidationError("Minimun salary should be 5000")
        return value

    def validate(self, data):
        print("Object validation")
        name = data.get('name')
        salary = data.get('salary')
        if name == 'shetty':
            if salary < 50000:
                raise serializers.ValidationError("Shetty's minimum salary should be 50000")
        return data
