import torch
import torch.nn as nn
import torch.optim as optim

# EarlyStopping 这是一个简单的early stopping的实现
class EarlyStopping:
    def __init__(self, patience=5, delta=0):
        self.patience = patience
        self.delta = delta
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.best_model = None

    def __call__(self, val_loss, model):
        score = -val_loss  # 因为我们希望最小化损失

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(model)
        elif score < self.best_score + self.delta:
            self.counter += 1
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = score
            self.save_checkpoint(model)
            self.counter = 0

    def save_checkpoint(self, model):
        self.best_model = model.state_dict()

# 示例训练代码
model = nn.Linear(10, 1)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters())
early_stopping = EarlyStopping(patience=3)

for epoch in range(50):  # 假设最大训练50轮
    # 模拟训练和验证过程
    train_loss = torch.rand(1).item()
    val_loss = torch.rand(1).item()  # 模拟验证损失

    print(f"Epoch {epoch}, Train Loss: {train_loss}, Val Loss: {val_loss}")
    early_stopping(val_loss, model)

    if early_stopping.early_stop:
        print("Early stopping triggered!")
        model.load_state_dict(early_stopping.best_model)  # 加载最佳模型
        break
