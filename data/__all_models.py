import sqlalchemy
from .db_session import SqlAlchemyBase


class Category(SqlAlchemyBase):
    __tablename__ = 'Категории'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'<Category> {self.id} {self.description}'


class Muscle(SqlAlchemyBase):
    __tablename__ = 'Мышцы'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    anatomy_desc = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    function_desc = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'<Muscle> {self.id} {self.name}'


class Exercise(SqlAlchemyBase):
    __tablename__ = 'Упражнения'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    scheme = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    category = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(Category.id), nullable=True)

    def __repr__(self):
        return f'<Exercise> {self.id} {self.name}'


class Difficulty(SqlAlchemyBase):
    __tablename__ = 'Сложности'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'<Difficulty> {self.id} {self.description}'


class Program(SqlAlchemyBase):
    __tablename__ = 'Программы тренировок'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    difficulty = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(Difficulty.id), nullable=True)

    def __repr__(self):
        return f'<Program> {self.id} {self.name}'


class ExerciseMuscle(SqlAlchemyBase):
    __tablename__ = 'Упражнения-Мышцы'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_exercise = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(Exercise.id), nullable=True)
    id_muscle = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(Muscle.id), nullable=True)

    def __repr__(self):
        return f'<ExerciseMuscle> {self.id}: {self.id_exercise} {self.id_muscle}'


class ProgramExercise(SqlAlchemyBase):
    __tablename__ = 'Программы-Упражнения'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_exercise = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(Exercise.id), nullable=True)
    id_program = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(Program.id), nullable=True)
    day_of_training = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    def __repr__(self):
        return f'<ProgramExercise> {self.id}: {self.id_exercise} {self.id_program}'
