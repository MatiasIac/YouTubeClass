using System;
using System.Diagnostics;
using System.IO;
using Microsoft.ML;
using Microsoft.ML.Core.Data;
using Microsoft.ML.Data;

namespace machinelearning
{
    public class IrisData
    {
        [LoadColumn(0)]
        public float SepalLength;

        [LoadColumn(1)]
        public float SepalWidth;

        [LoadColumn(2)]
        public float PetalLength;

        [LoadColumn(3)]
        public float PetalWidth;

        [LoadColumn(4)]
        public string Label;
    }

    public class IrisPrediction
    {
        [ColumnName("PredictedLabel")]
        public string PredictedLabels;
    }

    class Program
    {
        static void Main(string[] args)
        {
            var timer = new Stopwatch();
            timer.Start();

            var mlContext = new MLContext();

            ITransformer model;
            using (var stream = File.OpenRead("trainedModel")) {
                model = mlContext.Model.Load(stream);
            }

            /*var reader = mlContext.Data.CreateTextReader<IrisData>(separatorChar: ',', hasHeader: true);
            IDataView trainingDataView = reader.Read("iris.data");

            var pipeline = mlContext.Transforms.Conversion.MapValueToKey("Label")
                .Append(mlContext.Transforms.Concatenate("Features", "SepalLength", "SepalWidth", "PetalLength", "PetalWidth"))
                .Append(mlContext.MulticlassClassification.Trainers.StochasticDualCoordinateAscent(labelColumn: "Label", featureColumn: "Features"))
                .Append(mlContext.Transforms.Conversion.MapKeyToValue("PredictedLabel"));

            var model = pipeline.Fit(trainingDataView);

            using (var stream = File.Create("trainedModel"))
            {
                mlContext.Model.Save(model, stream);
            } */

            var prediction = model.CreatePredictionEngine<IrisData, IrisPrediction>(mlContext).Predict(
                new IrisData()
                {
                    SepalLength = 3.3f,
                    SepalWidth = 1.6f,
                    PetalLength = 0.2f,
                    PetalWidth = 5.1f,
                });

            Console.WriteLine($"Predicted flower type is: {prediction.PredictedLabels}");
            timer.Stop();
            Console.WriteLine(timer.Elapsed);
        }
    }
}
