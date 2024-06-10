from rest_framework import serializers
from.models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class UpdateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'objectives', 'start_date', 'end_date']
                
        def update(self, instance, validated_data):
            for field, value in validated_data.items():
                if getattr(instance, field)!= value:
                    setattr(instance, field, value)
            instance.save()
            return instance

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'assigned_to', 'start_date', 'end_date', 'status']
                
        def update(self, instance, validated_data):
            for field, value in validated_data.items():
                if getattr(instance, field)!= value:
                    setattr(instance, field, value)
            instance.save()
            return instance
