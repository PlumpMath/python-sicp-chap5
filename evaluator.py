#!/usr/bin/env python
# -*- coding: utf-8 -*-

from machine import *

class VariableUnassignedError(Error): pass

def is_self_evaluating(exp):
    if isinstance(exp, int): return True
    if isinstance(exp, long): return True
    if isinstance(exp, float): return True
    if isinstance(exp, str): return True

    return False

def is_variable(exp):
    if isinstance(exp, Symbol): return True

    return False

def is_quoted(exp):
    return is_tagged_list(exp, 'quote')

def is_assignment(exp):
    return is_tagged_list(exp, 'set!')

def is_definition(exp):
    return is_tagged_list(exp, 'define')

def is_if(exp):
    return is_tagged_list(exp, 'if')

def is_lambda(exp):
    return is_tagged_list(exp, 'lambda')

def is_begin(exp):
    return is_tagged_list(exp, 'begin')

def is_application(exp):
    return isinstance(exp, list)

def lookup_variable_value(exp, env):
    env_rev = env[:]
    env_rev.reverse()
    for frame in env_rev:
        if frame.has_key(exp):
            return frame[exp]

    raise VariableUnassignedError()

def text_of_quotation(exp):
    return exp[1]

def lambda_parameters(exp):
    return exp[1]

def lambda_body(exp):
    return exp[2:]

def make_procedure(parameters, body, env): # parameter, body, env
    return [Symbol(u'procedure')] + [parameters, body, env]

def operands(exp):
    return exp[1:]

def operator(exp):
    return exp[0]

def empty_arglist():
    return []

def is_no_operands(exp):
    return 0 == len(exp)

def first_operand(exp):
    return exp[0]

def is_last_operand(exp):
    return 0 == len(exp)

def adjoin_arg(arg, arglist):
    return arglist + [arg]

def rest_operands(exp):
    return exp[1:]

def is_primitive_procedure(exp):
    return is_tagged_list(exp, 'primitive')

def is_compound_procedure(exp):
    return is_tagged_list(exp, 'procedure')

the_primitive_procs = {
    '+' : lambda *args: reduce(lambda x,y: x+y, args),
    }
    
def apply_primitive_procedure(proc, *args):
    return the_primitive_procs[proc[1]](*args)

def procedure_parameters(proc):
    return proc[1]

def procedure_body(proc):
    return proc[2]

def procedure_environment(proc):
    return proc[3]

def extend_environment(vars, vals, base_env):
    return [dict(zip(vars, vals))] + base_env

def first_exp(seq):
    return seq[0]

def rest_exps(seq):
    return seq[1:]

def is_last_exp(seq):
    return 1 == len(seq)

def if_predicate(exp):
    return exp[1]

def if_consequent(exp):
    return exp[2]

def if_alternative(exp):
    try:
        return exp[3]
    except IndexError:
        return False

def assignment_variable(exp):
    return exp[1]

def assignment_value(exp):
    return exp[2]

def set_variable_value!(var, val, env):
    

ops = {
    'self-evaluating?' : is_self_evaluating,
    'variable?' : is_variable,
    'quoted?' : is_quoted,
    'assignment?' : is_assignment,
    'definition?' : is_definition,
    'if?' : is_if,
    'lambda?' : is_lambda,
    'begin?' : is_begin,
    'application?' : is_application,
    'lookup-variable-value' : lookup_variable_value,
    'text-of-quotation' : text_of_quotation,
    'lambda-parameters' : lambda_parameters,
    'lambda-body' : lambda_body,
    'make-procedure' : make_procedure,
    'operands' : operands,
    'operator' : operator,
    'empty-arglist' : empty_arglist,
    'no-operands?' : is_no_operands,
    'first-operand' : first_operand,
    'last-operand' : is_last_operand,
    'adjoin-arg' : adjoin_arg,
    'rest-operands' : rest_operands,
    'primitive-procedure?' : is_primitive_procedure,
    'compound-procedure?' : is_compound_procedure,
    'apply-primitive-procedure' : apply_primitive_procedure,
    'procedure-environment' : procedure_environment,
    'procedure-parameters' : procedure_parameters,
    'procedure-body' : procedure_body,
    'extend-environment' : extend_environment,
    'first-exp' : first_exp,
    'last-exp?' : is_last_exp,
    'if-predicate' : if_predicate,
    'if-consequent' : if_consequent,
    'if-alternative' : if_alternative,
    'assignment-variable' : assignment_variable,
    'assignment-value' : assignment_value,
}
