import {Entity, model, property, hasOne} from '@loopback/repository';
import {ErrorType} from './error-type.model';

@model({settings: {strict: false}})
export class StageErrorAction extends Entity {
  @property({
    type: 'number',
    required: true,
  })
  error_type_id: number;

  @property({
    type: 'number',
    required: true,
  })
  stage_id: number;

  @property({
    type: 'number',
    required: true,
  })
  action_type_id: number;

  @hasOne(() => ErrorType)
  errorType: ErrorType;
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<StageErrorAction>) {
    super(data);
  }
}

export interface StageErrorActionRelations {
  // describe navigational properties here
}

export type StageErrorActionWithRelations = StageErrorAction & StageErrorActionRelations;
