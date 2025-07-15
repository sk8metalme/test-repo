from flask import Blueprint, render_template, request, flash
from app.application.calculator_service import CalculatorService

bp = Blueprint('calculator', __name__)
service = CalculatorService()

@bp.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None
    left = right = operator = ''
    if request.method == 'POST':
        left = request.form.get('left', '')
        right = request.form.get('right', '')
        operator = request.form.get('operator', '')
        try:
            result = service.execute(left, right, operator)
            # 計算後はleftに結果をセットし、rightとoperatorをリセット
            left = str(result)
            right = ''
            operator = ''
        except Exception as e:
            error = str(e)
    return render_template('calculator.html', result=result, error=error, left=left, right=right, operator=operator)
