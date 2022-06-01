import papermill as pm

risk_score_models = ["Framingham"]

for model_name in risk_score_models:
   try:
      pm.execute_notebook(
         f'./{model_name}_Risk_Score_Unit_Tests.ipynb',
         f'./test_outputs/{model_name}_Risk_Score_Unit_Tests_Output.ipynb'
      )
   except pm.PapermillExecutionError as e:
      print(f"Exception Occurred -- {str(e)}")