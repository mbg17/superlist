class Pagination(object):
    """自定义分页（Bootstrap版）"""
    def __init__(self, page_num, all_data, base_url, per_page=10, max_page=11):
        """
        :param page_num: 当前请求的页码
        :param all_data: 总数据量
        :param base_url: 请求的URL
        :param per_page: 每页显示的数据量，默认值为10
        :param max_page: 页面上最多显示多少个页码，默认值为11
        """
        all_page = divmod(all_data, per_page)
        self.pages = all_page[0] + 1 if all_page[1] else all_page[0]
        try:
            self.page_num = int(page_num)
            if self.page_num > self.pages:
                self.page_num = self.pages
        except Exception as e:
            # 取不到或者页码数不是数字都默认展示第1页
            self.page_num = 1
        # 定义每页显示多少条数据
        self.per_page = per_page
        # 计算出总页码数
        # 定义页面上最多显示多少页码(为了左右对称，一般设为奇数)
        self.max_page = max_page
        self.half_page = max_page // 2
        self.base_url = base_url

    # 将方法变成静态属性
    # 页面显示规律 [(page_num-1)*per_page :page_num*per_page]
    @property
    def start(self):
        return (self.page_num-1) * self.per_page

    @property
    def end(self):
        return self.page_num * self.per_page

    @property
    def all_page(self):
        return self.pages

    def page_html(self):
        # 判断当前页数减去一半页数是否小于0
        if self.page_num - self.half_page < 1:
            page_start = 1
        else:
            page_start = self.page_num - self.half_page
        page_end = self.page_num + self.half_page + 1
        # 判断末尾页数是都大于总页数
        if page_end >= self.all_page:
            page_start = self.all_page - self.max_page + 1
            page_end = self.all_page
        else:
            page_end = self.page_num + self.half_page
        list_ = []
        # 拼接HTML
        if self.page_num > 1:
            list_.append(f'<li><a href="{self.base_url}?page={self.page_num - 1}" aria-label="Previous">&laquo</a></li>')
        else:
            list_.append('<li class="disabled"><a href="#" aria-label="Previous">&laquo</a></li>')
        for i in range(page_start, page_end + 1):
            if i == self.page_num:
                list_.append(f'<li class="active"><a href="{self.base_url}?page={i}">{i}</a></li>')
            else:
                list_.append(f'<li><a href="{self.base_url}?page={i}">{i}</a></li>')
        if self.page_num < self.all_page:
            list_.append(f'<li><a href="{self.base_url}?page={self.page_num + 1}" aria-label="Next">&raquo;</a></li>')
        else:
            list_.append('<li class="disabled"><a href="#" aria-label="Next">&raquo;</a></li>')
        page_list = ''.join(list_)
        return page_list