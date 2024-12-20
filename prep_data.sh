# model=unicamp-dl/mMiniLM-L6-v2-mmarco-v2 && batch_size=1024
# model=unicamp-dl/mt5-base-mmarco-v2 && batch_size=128

model=$1
batch_size=$2
device_id=$3

if [ -z "$device_id" ]; then
    device_id=0
fi

if [ -z "$model" ] || [ -z "$batch_size" ] || [ -z "$device_id" ]; then
    echo "Usage: $0 <model> <batch_size> <device_id>"
    exit 1
fi


CUDA_VISIBLE_DEVICES=$device_id python -m inpars.get_teacher_scores \
    --output_dir teacher-scores \
    --model $model \
    --batch_size $batch_size