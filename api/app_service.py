import json

class AppService:

    tasks = [
        {
            'id': 1,
            'clave_materia': "ACF-0901",
            'nombre_materia': "Cálculo Diferencial",
            'semestre': 1,
            'horas_practicas': 3,
            'horas_teoricas': 2,
            'total_horas': 5
        },
        {
            'id': 2,
            'clave_materia': "AED-1285",
            'nombre_materia': "Fundamentos de Programación",
            'semestre': 1,
            'horas_practicas': 2,
            'horas_teoricas': 3,
            'total_horas': 5
        },
        {
            'id': 3,
            'clave_materia': "ACA-0907",
            'nombre_materia': "Taller de Ética",
            'semestre': 1,
            'horas_practicas': 0,
            'horas_teoricas': 4,
            'total_horas': 5
        },
        {
            'id': 4,
            'clave_materia': "AEF-1041",
            'nombre_materia': "Matemáticas Discretas",
            'semestre': 1,
            'horas_practicas': 3,
            'horas_teoricas': 2,
            'total_horas': 5
        },
        {
            'id': 5,
            'clave_materia': "SCH-1024",
            'nombre_materia': "Taller de Administración",
            'semestre': 1,
            'horas_practicas': 1,
            'horas_teoricas': 3,
            'total_horas': 4
        },
        {
            'id': 6,
            'clave_materia': "ACC-0906",
            'nombre_materia': "Fundamentos de Investigación",
            'semestre': 1,
            'horas_practicas': 2,
            'horas_teoricas': 2,
            'total_horas': 4
        }
    ]

    def __init__(self):
        self.tasksJSON = json.dumps(self.tasks)

    def get_tasks(self):
        return self.tasksJSON

    def create_task(self,task):
        tasksData = json.loads(self.tasksJSON)
        tasksData.append(task)
        self.tasksJSON = json.dumps(tasksData)
        return self.tasksJSON

    def update_task(self, request_task):
        tasksData = json.loads(self.tasksJSON)
        for task in tasksData:
            if task["id"] == request_task['id']:
                task.update(request_task)
                return json.dumps(tasksData);
        return json.dumps({'message': 'task id not found'});

    def delete_task(self, request_task_id):
        tasksData = json.loads(self.tasksJSON)
        for task in tasksData:
            if task["id"] == request_task_id:
                tasksData.remove(task)
                return json.dumps(tasksData);
        return json.dumps({'message': 'task id not found'});