#-*- coding: UTF-8 -*-
from flask import Flask,render_template,session,redirect,url_for,flash,request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import SubmitField,FileField,StringField,SelectField
from wtforms.validators import Required
from werkzeug import secure_filename
import os,commands

#允许上传的文件的扩展名
ALLOWED_EXTENSIONS = set(['xls','xlsx'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

#定义上传文件表单类
class Upload(Form):
	file = FileField('Excel File:')
	submit = SubmitField('Submit')

#定义管理容器界面的表单类
class Mrg(Form):
	stuid = StringField('Please input Student ID:',validators=[Required()])
	sel = SelectField(u'Actions',choices=[('status','status'),('start','start'),('stop','stop'),('restart','restart')])
	submit = SubmitField('Submit')

#定义用户登录记录查询界面的表单类
class Lastlog(Form):
	stuid = StringField('Please input Student ID:',validators=[Required()])
	submit = SubmitField('Submit')

#定义C程序重复率检测界面的表单类
class CheckC(Form):
	submit = SubmitField('Start Check')

#定义历史命令查询界面的表单类
class History(Form):
	sel = SelectField(u'Role',choices=[('Server','Server'),('Client','Client')])
	stuid = StringField('Please input Student ID:',validators=[Required()])
	user = StringField('Please input username:',validators=[Required()])
	submit = SubmitField('Submit')

#默认路由
@app.route('/')
def index():
	return render_template('index.html')

#批量创建服务端容器页面的路由
@app.route('/bcresrv',methods=['GET','POST'])
def bcresrv():
	form = Upload()
	if form.validate_on_submit():
		session['filename'] = secure_filename(form.file.data.filename)
		if session.get('filename'):
			if session.get('filename').split('.')[-1] in ALLOWED_EXTENSIONS:
				form.file.data.save('uploads/' + session.get('filename'))
				cmd = "mydocker  --bcreatesrv  ./uploads/%s > /dev/null &" %session.get('filename')
				os.system(cmd)
				flash('The Server Containers is being created!')
				return redirect(url_for('index'))
			else:
				flash('Looks like you do not choose a excel file!')
				return redirect(url_for('bcresrv'))
		else:
			flash('Looks like you do not choose any file!')
			return redirect(url_for('bcresrv'))
	return render_template('bcresrv.html',form=form)

#批量创建客户端容器页面的路由
@app.route('/bcrecli',methods=['GET','POST'])
def bcrecli():
	form = Upload()
	if form.validate_on_submit():
		session['filename'] = secure_filename(form.file.data.filename)
		if session.get('filename'):
			if session.get('filename').split('.')[-1] in ALLOWED_EXTENSIONS:
				form.file.data.save('uploads/' + session.get('filename'))
				cmd = "mydocker  --bcreatecli  ./uploads/%s > /dev/null &" %session.get('filename')
				os.system(cmd)
				flash('The Client Containers is being created!')
				return redirect(url_for('index'))
			else:
				flash('Looks like you do not choose a excel file!')
				return redirect(url_for('bcrecli'))
		else:
			flash('Looks like you do not choose any file!')
			return redirect(url_for('bcrecli'))
	return render_template('bcrecli.html',form=form)

#批量删除服务端容器页面的路由
@app.route('/bdelsrv',methods=['GET','POST'])
def bdelsrv():
	form = Upload()
	if form.validate_on_submit():
		session['filename'] = secure_filename(form.file.data.filename)
		if session.get('filename'):
			if session.get('filename').split('.')[-1] in ALLOWED_EXTENSIONS:
				form.file.data.save('uploads/' + session.get('filename'))
				cmd = "mydocker  --bdelsrv  ./uploads/%s > /dev/null &" %session.get('filename')
				os.system(cmd)
				flash('The Server Containers is being deleted!')
				return redirect(url_for('index'))
			else:
				flash('Looks like you do not choose a excel file!')
				return redirect(url_for('bdelsrv'))
		else:
			flash('Looks like you do not choose any file!')
			return redirect(url_for('bdelsrv'))
	return render_template('bdelsrv.html',form=form)

#批量删除客户端容器页面的路由
@app.route('/bdelcli',methods=['GET','POST'])
def bdelcli():
	form = Upload()
	if form.validate_on_submit():
		session['filename'] = secure_filename(form.file.data.filename)
		if session.get('filename'):
			if session.get('filename').split('.')[-1] in ALLOWED_EXTENSIONS:
				form.file.data.save('uploads/' + session.get('filename'))
				cmd = "mydocker  --bdelcli  ./uploads/%s > /dev/null &" %session.get('filename')
				os.system(cmd)
				flash('The Client Containers is being deleted!')
				return redirect(url_for('index'))
			else:
				flash('Looks like you do not choose a excel file!')
				return redirect(url_for('bdelcli'))
		else:
			flash('Looks like you do not choose any file!')
			return redirect(url_for('bdelcli'))
	return render_template('bdelcli.html',form=form)

#管理服务端容器页面的路由
@app.route('/mrgsrv',methods=['GET','POST'])
def mrgsrv():
	form = Mrg()
	if form.validate_on_submit():
		session['stuid'] = form.stuid.data
		session['sel'] = form.sel.data
		if session.get('sel') == 'status':
			(status,output) = commands.getstatusoutput("mydocker --%ssrv %s" %(session.get('sel'),session.get('stuid')))
			flash('<pre>' + output + '</pre>')
			return redirect(url_for('mrgsrv'))
		else:
			(status,output) = commands.getstatusoutput("mydocker --%ssrv %s" %(session.get('sel'),session.get('stuid')))
			if status == 0:
				flash('Successful operation!')
				return redirect(url_for('mrgsrv'))
			else:
				flash('The Student ID error or does not exist!')
				return redirect(url_for('mrgsrv'))
	return render_template('mrgsrv.html',form=form)

#管理客户端容器页面的路由
@app.route('/mrgcli',methods=['GET','POST'])
def mrgcli():
	form = Mrg()
	if form.validate_on_submit():
		session['stuid'] = form.stuid.data
		session['sel'] = form.sel.data
		if session.get('sel') == 'status':
			(status,output) = commands.getstatusoutput("mydocker --%scli %s" %(session.get('sel'),session.get('stuid')))
			flash('<pre>' + output + '</pre>')
			return redirect(url_for('mrgcli'))
		else:
			(status,output) = commands.getstatusoutput("mydocker --%scli %s" %(session.get('sel'),session.get('stuid')))
			if status == 0:
				flash('Successful operation!')
				return redirect(url_for('mrgcli'))
			else:
				flash('The Student ID error or does not exist!')
				return redirect(url_for('mrgcli'))
	return render_template('mrgcli.html',form=form)

#服务端容器用户登录记录查询页面的路由
@app.route('/srvlastlog',methods=['GET','POST'])
def srvlastlog():
	form = Lastlog()
	if form.validate_on_submit():
		session['stuid'] = form.stuid.data
		(status,output) = commands.getstatusoutput("mydocker --srvlastlog %s" %session.get('stuid'))
		if status == 0:
			flash('<pre>' + output + '</pre>')
			return redirect(url_for('srvlastlog'))
		else:
			flash('The Student ID error or does not exist!')
			return redirect(url_for('srvlastlog'))
	return render_template('srvlastlog.html',form=form)
		
#客户端容器用户登录记录查询页面的路由
@app.route('/clilastlog',methods=['GET','POST'])
def clilastlog():
	form = Lastlog()
	if form.validate_on_submit():
		session['stuid'] = form.stuid.data
		(status,output) = commands.getstatusoutput("mydocker --clilastlog %s" %session.get('stuid'))
		if status == 0:
			flash('<pre>' + output + '</pre>')
			return redirect(url_for('clilastlog'))
		else:
			flash('The Student ID error or does not exist!')
			return redirect(url_for('clilastlog'))
	return render_template('clilastlog.html',form=form)

#服务端C程序重复率检测页面的路由
@app.route('/chksrvc',methods=['GET','POST'])
def chksrvc():
	form = CheckC()
	if form.validate_on_submit():
		(status,output) = commands.getstatusoutput("mydocker --checkserverc")
		flash('<pre>' + output + '</pre>')
		return redirect(url_for('chksrvc'))
	return render_template('chksrvc.html',form=form)

#客户端C程序重复率检测页面的路由
@app.route('/chkclic',methods=['GET','POST'])
def chkclic():
	form = CheckC()
	if form.validate_on_submit():
		(status,output) = commands.getstatusoutput("mydocker --checkclientc")
		flash('<pre>' + output + '</pre>')
		return redirect(url_for('chkclic'))
	return render_template('chkclic.html',form=form)

#历史命令查询页面的路由
@app.route('/history',methods=['GET','POST'])
def history():
	form = History()
	if form.validate_on_submit():
		session['sel'] = form.sel.data
		session['stuid'] = form.stuid.data
		session['user'] = form.user.data
		(status,output) = commands.getstatusoutput("mydocker --history %s %s %s" %(session.get('sel'),session.get('stuid'),session.get('user')))
		flash('<pre>' + output + '</pre>')
		return redirect(url_for('history'))
	return render_template('history.html',form=form)

#404页面的路由
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

if __name__ == '__main__':
	app.run('0.0.0.0')
