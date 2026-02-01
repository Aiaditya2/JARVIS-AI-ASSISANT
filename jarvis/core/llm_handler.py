# -*- coding: utf-8 -*-
"""
Local LLM Handler
Supports multiple LLM backends optimized for low RAM usage
"""

import logging
import sys
from typing import Optional, Dict, Any
import os

# Fix encoding for Windows
if sys.platform == 'win32':
    try:
        import codecs
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        if hasattr(sys.stderr, 'buffer'):
            sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except Exception:
        pass

logger = logging.getLogger(__name__)


class LLMHandler:
    """Handles local LLM inference with low RAM requirements"""
    
    def __init__(self, model_type: str = "ollama", model_name: str = "llama3.2:1b"):
        """
        Initialize LLM handler
        
        Args:
            model_type: Backend type ('ollama', 'transformers', 'llama_cpp')
            model_name: Model identifier
        """
        self.model_type = model_type
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize the LLM model based on type"""
        try:
            if self.model_type == "ollama":
                self._init_ollama()
            elif self.model_type == "transformers":
                self._init_transformers()
            elif self.model_type == "llama_cpp":
                self._init_llama_cpp()
            else:
                logger.warning(f"Unknown model type: {self.model_type}")
        except Exception as e:
            logger.error(f"Failed to initialize model: {e}")
    
    def _init_ollama(self):
        """Initialize Ollama backend (recommended for low RAM)"""
        try:
            import ollama
            self.client = ollama.Client()
            logger.info(f"Ollama initialized with model: {self.model_name}")
        except ImportError:
            logger.error("Ollama not installed. Install with: pip install ollama")
        except Exception as e:
            logger.error(f"Ollama initialization error: {e}")
    
    def _init_transformers(self):
        """Initialize Transformers backend with quantized models"""
        try:
            from transformers import AutoModelForCausalLM, AutoTokenizer
            import torch
            
            # Use quantized models for low RAM
            logger.info(f"Loading quantized model: {self.model_name}")
            
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            
            # Load with 8-bit quantization
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                torch_dtype=torch.float16,
                device_map="auto",
                load_in_8bit=True
            )
            logger.info("Transformers model loaded successfully")
        except ImportError:
            logger.error("Transformers not installed")
        except Exception as e:
            logger.error(f"Transformers initialization error: {e}")
    
    def _init_llama_cpp(self):
        """Initialize llama.cpp backend (most efficient for low RAM)"""
        try:
            from llama_cpp import Llama
            
            model_path = os.path.join("models", f"{self.model_name}.gguf")
            if not os.path.exists(model_path):
                logger.warning(f"Model file not found: {model_path}")
                return
            
            self.model = Llama(
                model_path=model_path,
                n_ctx=2048,
                n_threads=4,
                verbose=False
            )
            logger.info("llama.cpp model loaded successfully")
        except ImportError:
            logger.error("llama-cpp-python not installed")
        except Exception as e:
            logger.error(f"llama.cpp initialization error: {e}")
    
    def generate(self, prompt: str, max_tokens: int = 150, temperature: float = 0.7) -> str:
        """
        Generate response from LLM
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            
        Returns:
            Generated text
        """
        try:
            if self.model_type == "ollama":
                return self._generate_ollama(prompt, max_tokens, temperature)
            elif self.model_type == "transformers":
                return self._generate_transformers(prompt, max_tokens, temperature)
            elif self.model_type == "llama_cpp":
                return self._generate_llama_cpp(prompt, max_tokens, temperature)
            else:
                return "LLM not properly initialized"
        except Exception as e:
            logger.error(f"Generation error: {e}")
            return f"Error: {str(e)}"
    
    def _generate_ollama(self, prompt: str, max_tokens: int, temperature: float) -> str:
        """Generate using Ollama"""
        try:
            response = self.client.generate(
                model=self.model_name,
                prompt=prompt,
                options={
                    "num_predict": max_tokens,
                    "temperature": temperature
                }
            )
            return response.get("response", "")
        except Exception as e:
            logger.error(f"Ollama generation error: {e}")
            return ""
    
    def _generate_transformers(self, prompt: str, max_tokens: int, temperature: float) -> str:
        """Generate using Transformers"""
        try:
            inputs = self.tokenizer(prompt, return_tensors="pt")
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=temperature,
                do_sample=True
            )
            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            logger.error(f"Transformers generation error: {e}")
            return ""
    
    def _generate_llama_cpp(self, prompt: str, max_tokens: int, temperature: float) -> str:
        """Generate using llama.cpp"""
        try:
            response = self.model(
                prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                stop=["\n\n", "User:", "Assistant:"]
            )
            return response["choices"][0]["text"]
        except Exception as e:
            logger.error(f"llama.cpp generation error: {e}")
            return ""
