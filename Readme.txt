**🚀 Proyecto de Clasificación de Imágenes con Redes Neuronales Convolucionales (CNNs) 🌱**

**Descripción del Proyecto:**

Recientemente, he completado un proyecto emocionante que se centra en la clasificación de imágenes de plantas mediante el uso de redes neuronales convolucionales (CNNs). Este proyecto incluyó la comparación de dos estrategias distintas para abordar un problema de clasificación de 12 tipos diferentes de plantas. A continuación, se detallan las etapas del proyecto y los resultados obtenidos.

**🔍 Pipeline de Desarrollo:**

1. **Carga e Inspección del Dataset:**
   - Importación y exploración inicial del dataset para comprender mejor sus características y estructura.

2. **Acondicionamiento de los Datos:**
   - Aplicación de técnicas de preprocesamiento, incluyendo normalización y data augmentation, para mejorar la calidad del entrenamiento y la generalización del modelo.

3. **Desarrollo y Entrenamiento del Modelo:**
   - Diseño de una red neuronal convolucional desde cero y comparación de su rendimiento con varios modelos preentrenados utilizando técnicas de transfer learning.

4. **Evaluación y Monitorización:**
   - Monitoreo de las curvas de aprendizaje y ajuste de los hiperparámetros para optimizar el rendimiento del modelo.

**🧠 Estrategia 1: Entrenamiento desde Cero**

- En esta estrategia, diseñé y entrené una red neuronal profunda desde cero. Utilicé técnicas avanzadas de regularización, como dropout, batch normalization y weight regularization, logrando una precisión competitiva en la clasificación de las imágenes.

**🤖 Estrategia 2: Transfer Learning con Redes Preentrenadas**

- Implementé transfer learning utilizando modelos preentrenados como VGG16, ResNet50V2 y MobileNetV2. Tras comparar estas arquitecturas, el modelo ajustado con fine-tuning sobre MobileNetV2 mostró la mayor precisión, superando al modelo entrenado desde cero.

**📊 Resultados y Conclusiones:**

- La estrategia de transfer learning demostró ser más efectiva, alcanzando una mayor precisión con un tiempo de entrenamiento significativamente menor. Este hallazgo subraya la potencia de utilizar modelos preentrenados cuando los recursos computacionales y el tiempo son limitados.

**🔧 Herramientas y Tecnologías Utilizadas:**

- Utilicé TensorFlow, Keras, Scikit-learn y Seaborn para todo el flujo de trabajo, desde la preparación de datos hasta la visualización de resultados. El proyecto se ejecutó en Google Colab y el dataset se descargó desde Kaggle.

**📷 Visualización de Resultados:**

- Incluyo visualizaciones clave como tablas resumen de los resultados obtenidos con las distintas arquitecturas, curvas de aprendizaje y matrices de confusión, que ayudan a monitorizar el rendimiento del modelo durante el entrenamiento.

**Enlace al Repositorio:**

Puedes explorar los notebooks y el código fuente completo del proyecto en el siguiente enlace: [Proyectos de IA en GitHub](https://github.com/JuanArocaMIAR/Proyectos-IA)

**Contacto:**

Para cualquier pregunta o colaboración, no dudes en contactarme a través de juan.arocap@outlook.es o en .