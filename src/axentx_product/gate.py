from typing import Dict, Any

class QualityGate:
    """
    A hard-gate for product validation within the Axentx OS pipeline.
    Ensures a product has validated pain and willingness-to-pay before shipping.
    """
    def validate(self, product: Dict[str, Any]) -> bool:
        """
        Validates a product dictionary.
        Returns True if 'pain_score' > 0 and 'willingness_to_pay' > 0.
        """
        if not isinstance(product, dict):
            return False
            
        pain = product.get("pain_score", 0)
        wtp = product.get("willingness_to_pay", 0)
        
        return (
            isinstance(pain, (int, float)) and 
            isinstance(wtp, (int, float)) and 
            pain > 0 and 
            wtp > 0
        )
