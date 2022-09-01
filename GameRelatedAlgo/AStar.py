#!usr/bin/env python
# A*用来解决什么问题？
# 计算玩家行进的最短路径，可以避开中间的阻挡找到最短路径。

# 基本原理
# 不停地找周围的点，选出一个新的点作为起点再循环地找，直到找到终点。

# 详细原理
# 1.寻路消耗公式: f = g + h
# g: 离起点的距离（上下左右1，斜边1.4）
# h: 离终点的距离，曼哈顿距离
# 2.开启列表(集合概念)：将要去寻找的最优点
#   放入开启列表判断：不是阻挡、不在开启或者关闭列表内。
# 3.关闭列表(集合)：找到的最优点
#   放入关闭列表判断：判断是否终点（结束）、如果不是继续寻路。
# 4.格子对象的父对象：用于确定最终的路径。
#   被派生的对象的父对象即该对象。
# 5.死路如何确定？
#   开启列表为空的情况下，就是死路了。
cell_dict = {}

class Cell(object):
    def __init__(self, own_id, parent_id, pos, start_point, end_point, parent_start_cost):
        self._id = own_id
        self.parent_id = parent_id
        self.parent_start_cost = parent_start_cost
        self.pos = pos
        self.start_point = start_point
        self.end_point = end_point
        self.cost = 0
        self.cost_start = 0
        self.cost_end = 0
        self._compute_cost()

    def _compute_cost(self):
        y, x = self.pos
        y_s, x_s = cell_dict[self.parent_id].pos if self.parent_id else self.start_point
        y_e, x_e = self.end_point
        if self.pos == self.start_point:
            self.cost_start = 0
        elif abs(x - x_s) + abs(y - y_s) >= 2:
            self.cost_start = 1.4 + self.parent_start_cost
        else:
            self.cost_start = 1 + self.parent_start_cost
        self.cost_end = abs(x_e - x) + abs(y_e - y)
        self.cost = self.cost_start + self.cost_end

    def get_id(self):
        return self._id

    def get_cost_start(self):
        return self.cost_start

    def get_cost_end(self):
        return self.cost_end

    def get_cost(self):
        return self.cost

    def get_parent(self):
        return self.parent_id


next_point_dir_list = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
class AStar(object):
    def __init__(self, input_map, start_point, end_point):
        self._id_generate = 0
        self.map = input_map
        self.l_map, self.r_map, self.t_map, self.b_map = 0, len(input_map[0]) - 1, 0, len(input_map) - 1 
        self.start_point = start_point
        self.start_cell = self.gen_cell(None, start_point, start_point, end_point, 0)
        self.end_point = end_point
        self.open_list = []
        self.close_list = []
        self.found_path = False
        self._compute_closest_path()

    def gen_cell(self, parent_id, pos, start_point, end_point, parent_start_cost):
        tmp_id = self.gen_id()
        cell_dict[tmp_id] = Cell(tmp_id, parent_id, pos, start_point, end_point, parent_start_cost)
        return cell_dict[tmp_id]

    def gen_id(self):
        self._id_generate += 1
        return self._id_generate

    def _compute_closest_path(self):
        y_s, x_s = self.start_point
        for next_point_dir in next_point_dir_list:
            dir_y, dir_x = next_point_dir
            y_next, x_next = y_s + dir_y, x_s + dir_x
            if self._valid_point((y_next, x_next)):
                tmp_cell = self.gen_cell(self.start_cell.get_id(), (y_next, x_next), self.start_point, self.end_point, self.start_cell.get_cost_start())
                self.open_list.append(tmp_cell)
        self.close_list.append(self.start_cell)

        found_closest_way = False
        while self.open_list and not found_closest_way:
            self.open_list.sort(key=lambda c: c.get_cost())
            choose_cell = self.open_list[0]
            self.open_list = self.open_list[1:]
            self.close_list.append(choose_cell)
            if choose_cell.pos == self.end_point:
                found_closest_way = True
                continue

            new_y_s, new_x_s = choose_cell.pos
            for next_point_dir in next_point_dir_list:
                dir_y, dir_x = next_point_dir
                y_next, x_next = new_y_s + dir_y, new_x_s + dir_x
                if self._valid_point((y_next, x_next)):
                    tmp_cell = self.gen_cell(choose_cell.get_id(), (y_next, x_next), self.start_point, self.end_point, choose_cell.get_cost_start())
                    self.open_list.append(tmp_cell)

        if not self.open_list:
            print('not exist such path')
            self.found_path = False
        else:
            self.found_path = True



            
    def _valid_point(self, pos):
        y, x = pos
        if x < self.l_map or x > self.r_map:
            return False
        if y < self.t_map or y > self.b_map:
            return False
        if self.map[y][x]:
            return False
        for cell in self.open_list:
            if cell.pos == pos:
                return False
        for cell in self.close_list:
            if cell.pos == pos:
                return False
        return True

    def get_closest_path(self):
        result = []
        if not self.found_path:
            return []
        last_add_end_cell = self.close_list[-1]
        while last_add_end_cell.pos != self.start_point:
            parent_id = last_add_end_cell.get_parent()
            result.append(last_add_end_cell.pos)
            last_add_end_cell = cell_dict[parent_id]
        result.append(self.start_point)
        return result


if __name__ == "__main__":
    input_map = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    a_star = AStar(input_map, (1, 1), (1, 3))
    result = a_star.get_closest_path()
    result.reverse()
    print(result)

