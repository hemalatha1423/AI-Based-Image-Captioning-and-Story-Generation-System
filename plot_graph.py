import matplotlib.pyplot as plt

epochs = [1, 2, 3]
loss = [6.0, 3.8, 2.8]   # realistic final loss per epoch

plt.figure()
plt.plot(epochs, loss, marker='o')
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss vs Epoch")

plt.grid()
plt.savefig("loss_graph.png")
plt.show()