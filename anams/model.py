import os
import numpy as np

# Orange 라이브러리 임포트
try:
    import Orange
    from Orange.data import Table, Domain, ContinuousVariable
except ImportError:
    Orange = None
    print("경고: Orange 라이브러리를 찾을 수 없습니다. pip install orange3 로 설치하세요.")

# 모델 파일 경로 (이 파일과 같은 디렉토리에 있어야 합니다)
MODEL_FILES = {
    'rnn': 'neural.pkcls',
    'svm': 'SVM.pkcls',
    'knn': 'kNN.pkcls'
}

LOADED_MODELS = {}

def load_orange_models():
    """앱 시작 시 Orange 모델 파일들을 로드하여 전역 변수에 저장합니다."""
    global LOADED_MODELS
    if not Orange:
        return False

    print("\n--- Orange 모델 로드 시작 ---")
    
    # 이미 로드된 경우 다시 로드하지 않음
    if LOADED_MODELS:
        print("이미 로드된 모델이 있습니다.")
        return True

    success = True
    for key, filename in MODEL_FILES.items():
        try:
            # 파일 존재 여부 확인
            if not os.path.exists(filename):
                print(f"오류: {filename} 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
                LOADED_MODELS[key] = None
                success = False
                continue

            model = Orange.classification.load(filename)
            LOADED_MODELS[key] = model
            print(f"성공: {filename} 로드 완료.")
        except Exception as e:
            print(f"오류: {filename} 로드 실패. 오류: {e}")
            LOADED_MODELS[key] = None
            success = False
            
    print("--- 모델 로드 완료 ---")
    return success

def predict_with_orange_models(data_input):
    """
    입력 데이터를 받아 로드된 Orange 모델들을 사용하여 예측을 수행합니다.
    """
    if not Orange or not any(LOADED_MODELS.values()):
        return {"RNN": "라이브러리/모델 없음", "SVM": "라이브러리/모델 없음", "kNN": "라이브러리/모델 없음"}

    try:
        # 입력 특징 정의 (순서는 모델 학습 시 사용한 순서와 일치해야 합니다)
        features = [
            ContinuousVariable('weight'), ContinuousVariable('height'), ContinuousVariable('heartRate'),
            ContinuousVariable('targetWeight'), ContinuousVariable('targetDuration'),
            ContinuousVariable('workoutDays'), ContinuousVariable('workoutTime'),
        ]
        test_domain = Domain(features)

        # 입력값을 Orange Table 형태로 변환 (data_input은 딕셔너리 형태여야 함)
        data_vector = [
            data_input['weight'], data_input['height'], data_input['heartRate'],
            data_input['targetWeight'], data_input['targetDuration'],
            data_input['workoutDays'], data_input['workoutTime'],
        ]
        data_instance = Table(test_domain, [data_vector])

        predictions = {}

        # 각 모델별 예측 수행
        for key, model in LOADED_MODELS.items():
            if model:
                prediction_index = int(model(data_instance)[0])
                class_name = model.domain.class_var.values[prediction_index]
                predictions[key.upper()] = class_name
            else:
                predictions[key.upper()] = "모델 로드 실패"

        return predictions

    except Exception as e:
        print(f"예측 처리 중 모듈 오류 발생: {e}")
        return {"RNN": f"오류: {e}", "SVM": f"오류: {e}", "kNN": f"오류: {e}"}

# 모델 초기 로드 시도
load_orange_models()
