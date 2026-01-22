
from model_service import ModelService

def main():
    ml_svc = ModelService()
    ml_svc.load_model('rf_v1')
    predict = ml_svc.predict([50, 2000, 2, 10, 1, 0, 1, 0, 1])
    print(predict)

if __name__ == "__main__":
    main()