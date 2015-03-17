from django.utils.safestring import mark_safe


def pager(baseurl, currentpage, totalcount, totalpage, pagernum=11):
	currentpage = int(currentpage)
	totalpage = int(totalpage)
	if currentpage >= totalpage:
		currentpage = totalpage
	pagernum = int(pagernum)
	prev = currentpage - 1
	Next = currentpage + 1
	if currentpage <= 1:
		prev_str = '<li class="disabled"><a href="#">上一页</a></li>'
	else:
		prev_str = '<li><a href="#" onclick="ChangePager(%d);return false;">上一页</a></li>' % (currentpage - 1,)

	if Next >= totalpage:
		next_str = '<li class="disabled"><a href="#">下一页</a></li>'
	else:
		next_url = baseurl + str(currentpage + 1)
		next_str = '<li><a href="#" onclick="ChangePager(%d);return false;">下一页</a></li>' % (currentpage + 1,)

	first_str = '<li><a href="#" onclick="ChangePager(%d);return false;">首页</a></li>' % (1,)
	end_str = '<li><a href="#" onclick="ChangePager(%d);return false;">末页</a></li>' % (totalpage,)
	pagelist = []

	start = 1 if currentpage - 5 < 1 else currentpage - 5
	if start < 6:
		end = 11
	else:
		end = totalpage if currentpage + 5 > totalpage else currentpage + 5
	if end > totalpage:
		end = totalpage

	for i in range(start, end + 1):
		url = baseurl + str(i)
		if currentpage == i:
			pagelist.append(
				'<li class="active"><a href="#" onclick="ChangePager(%d);return false;">%d</a></li>' % (i, i,))
		else:
			pagelist.append('<li><a href="#" onclick="ChangePager(%d);return false;">%d</a></li>' % (i, i,))
	total_str = ('<li><a href="javascript:void(0);">共 %d 页/ %d 条数据</a></li>' % (totalpage, totalcount,))
	result = first_str + prev_str + ''.join(pagelist) + next_str + end_str + total_str

	return mark_safe(result)