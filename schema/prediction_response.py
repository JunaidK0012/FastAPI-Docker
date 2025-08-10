from pydantic import BaseModel, Field
from typing import Annotated,Dict 

class PredictionResponse(BaseModel):

    predicted_category: Annotated[str, Field(...,description="The predicted insurance premium category",example='High')]

    confidence: Annotated[float, Field(...,description="Models comfidence score for the predicetd class(rangeL: 0 to 1)",example=0.8432)]

    class_probabilities: Annotated[Dict[str,float], Field(...,description="Probability distribution across all possible classes",
        example={"Low": 0.01, "Medium": 0.15, "High": 0.84}
    )]