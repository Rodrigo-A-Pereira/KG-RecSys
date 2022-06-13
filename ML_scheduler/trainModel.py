
import os
try:
    import pykeen
    from pykeen.pipeline import pipeline
    from pykeen.trackers import PythonResultTracker
    from PykeenMLFlowWrapper import save_model
    import mlflow
    from mlflow.tracking import MlflowClient

    mlflow.set_tracking_uri("http://mlflow-server:5000")
    tracker = PythonResultTracker()
    pipeline_result = pipeline(
        training='/ML_dir/trainingFile.txt',
        testing='/ML_dir/trainingFile.txt',
        model='TransE',
        model_kwargs=dict(
            embedding_dim=2000
        ),

        epochs=1000,
        result_tracker=tracker,

    )
    s=save_model(pipeline_result, "","recsys_transe", tracker)
    client=MlflowClient()
    client.transition_model_version_stage(
        name="recsys_transe",
        version=max([int(x.version) for x in client.get_latest_versions("recsys_transe")]),
        stage="Production"
    )

except Exception as e: 
    print(f"Exception: {str(e)}\n")
