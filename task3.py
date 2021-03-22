from itertools import cycle
from flask import Flask, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)


class Timing(Resource):
    def get(self):
        json_data = json.loads(request.data)
        print(type(json_data["lesson"]))
        result = appearance(json_data)
        return {'result': result}, 200


def checks(data, lesson, intervals, length):
    t_timings = []
    lesson_start = lesson[0]
    lesson_end = lesson[1]
    for t in range(0, length, 2):
        t_next = next(data)
        t_start, t_next = t_next, next(data)
        if t_start <= lesson_end and t_next >= lesson_start:
            if t_start <= lesson_start:
                t_start = lesson_start
            if t_next >= lesson_end:
                t_next = lesson_end
            t_timings.append([t_start, t_next])
    return t_timings


def pupil_x_tutor(p_timings, t_timings):
    time = 0
    for p_timing in p_timings:
        p_start = p_timing[0]
        p_end = p_timing[1]
        for t_timing in t_timings:
            t_start = t_timing[0]
            t_end = t_timing[1]
            if p_start <= t_end and p_end >= t_start:
                time += (max(p_end, t_end) - (min(p_start, t_start))) - (
                        max(t_start, p_start) - min(t_start, p_start)) - (max(t_end, p_end) - min(t_end, p_end))
    return time


def appearance(intervals):
    lesson = intervals['lesson']
    print(lesson)
    pupils = cycle(intervals['pupil'])
    tutors = cycle(intervals['tutor'])
    p_timings = checks(pupils, lesson, intervals, len(intervals['pupil']))
    t_timings = checks(tutors, lesson, intervals, len(intervals['tutor']))
    answer = pupil_x_tutor(p_timings, t_timings)
    return answer


api.add_resource(Timing, "/timing", "/timing/")

if __name__ == '__main__':
    app.run(debug=True)
