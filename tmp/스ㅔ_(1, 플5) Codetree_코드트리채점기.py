# 18:14~19:25

# (1, 플5) Codetree_코드트리채점기


# 채점기: Judger      [상태,
# task                  TODO: [우선순위, 타임스탬프, 도메인, id]

import heapq
from typing import List


class Task:
    def __init__(self, priority, timestamp, url):
        self.priority = priority
        self.timestamp = timestamp
        self.url = url
        self.domain, self.id = url.split('/')

    def __str__(self):
        return f"p: {self.priority}, time: {self.timestamp}, url: {self.url}"

    def __le__(self, other):
        if self.priority < other.priority:
            return True
        elif self.timestamp < other.timestamp:
            return True

    def get_domain(self):
        return self.domain


class WaitingQueue:

    def __init__(self):
        self.priority_queue: List[Task]= []
        self.url_set = set()

    def add_task(self, task: Task):
        heapq.heappush(self.priority_queue, task)
        self.url_set.add(task.url)

    def check_url(self, url):
        return url in self.url_set

    def pop_task(self) -> Task:
        if not self.priority_queue:
            return None
        self.url_set.remove(self.priority_queue[0].url)
        return heapq.heappop(self.priority_queue)


class MachineManager:

    def __init__(self, n):
        self.unused_pq = list(range(1, n + 1))
        heapq.heapify(self.unused_pq)
        self.used_status = [None] * (n + 1)
        self.domain_dict = dict()               # 도메인: [이전 시작 시간, 이전 종료 시간]

    def get_unused_machine(self):
        if not self.unused_pq:
            return None
        return heapq.heappop(self.unused_pq)

    def start_judging(self, timestamp, machine_id, task: Task):
        self.domain_dict[task.get_domain()] = [timestamp, 0]
        self.used_status[machine_id] = task.get_domain()

    def stop_judging(self, timestamp, machine_id):
        domain = self.used_status[machine_id]
        self.domain_dict[domain][1] = timestamp

        self.used_status[machine_id] = None
        heapq.heappush(self.unused_pq, machine_id)

    def check_if_used_machine(self, machine_id):
        return self.used_status[machine_id] is not None

    def check_if_domain_exists(self, domain):
        if domain not in self.domain_dict:
            return False
        else:
            if self.domain_dict[domain][1] == 0:      # 사용 중
                return True
            else:
                return False

    def check_if_inappropriate_judging(self, timestamp, domain):
        # 가장 최근에 진행된 채점 시작 시간 == start, 종료 시간 start+gap 였고
        # t < start + 3 * gap 인 경우
        if domain not in self.domain_dict:
            return False

        start, end = self.domain_dict[domain]
        return timestamp < start + 3 * (end - start)


waiting_queue = WaitingQueue()
machine_manager: MachineManager = None


# (100) 코드트리 채점기 준비 N, u_0
def prepare_machine(n, u_0):
    global waiting_queue, machine_manager
    machine_manager = MachineManager(n)
    waiting_queue.add_task(Task(1, 0, u_0))

    # N개 채점기
    # url == u_0 [도메인/문제ID]
    # 0초 -> priority==1 && url==u_0인 문제에 대한 채점 요청
    # 채점 task는 채점 대기 큐에 들어간다                TODO: add([1, 0초, domain/id])


# (200) 채점 요청 t, p, u
def request_judging(timestamp, priority, url):
    # t초 -> priority==p && url==u인 문제에 대한 채점 요청
    # 채점 task는 채점 대기 큐에 추가된다.
    # 대기 큐 task 중 url==u인 요청이 있다면 추가하지 않는다. TODO: waiting_queue.check
    if not waiting_queue.check_url(url):
        waiting_queue.add_task(Task(priority, timestamp, url))


# (300) 채점 시도 t
def try_judging(timestamp):
    global machine_manager, waiting_queue
    # t초 -> 대기 큐에서 우선순위가 가장 높은 task를 골라 채점 진행

    # 채점이 가능한 경우 중 우선순위가 높은 채점 task
    #   min(p)
    #   min(timestamp)

    task_list = []
    curr_task = waiting_queue.pop_task()

    # task가 채점 될 수 없는 조건
    while curr_task:
        # - task의 도메인이 현재 채점을 진행 중인 도메인 중 하나인 경우 TODO: 현재 도메인
        if machine_manager.check_if_domain_exists(curr_task.get_domain()):
            task_list.append(curr_task)
            curr_task = waiting_queue.pop_task()
            continue
        # - task의 도메인과 정확히 일치하는 도메인에 대해,            TODO: 이전 도메인
        if machine_manager.check_if_inappropriate_judging(timestamp, curr_task.get_domain()):
            task_list.append(curr_task)
            curr_task = waiting_queue.pop_task()
            continue

    if curr_task:
    # t초에 채점이 가능한 task O ->

        unused_machine = machine_manager.get_unused_machine()
        #   쉬고 있는 채점기 O ->
        if unused_machine:
        #       min 번호 채점기가
        #       우선순위가 가장 높은 채점 task에 대한 채점 시작
            machine_manager.start_judging(unused_machine)
        #   쉬고 있는 채점기 X -> 넘겨

# (400) 채점 종료 t, J_id
# J_id 채점기가 진행하던 채점 종료      TODO: machine 상태 변경

# (500) 채점 대기 큐 조회
# 채점 task 수 출력
